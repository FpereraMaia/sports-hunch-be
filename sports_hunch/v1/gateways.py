from bet_details.models import BetDetails
from bets.enums import BetStatus
from bets.models import BetRanking
from core.adapters.gateways import ChampionshipAdapter, BettorAdapter, BetAdapter
from core.domains.championship import Championship, BetStandings
from core.entities import Ranking
from typing import List
from users.models import User
from v1.ranking.models import ChampionshipTable, Standings as StandingsModel


class ChampionshipGateway(ChampionshipAdapter):
    def get_championships_without_ranking(self) -> List[Championship]:
        championships = ChampionshipTable.objects.prefetch_related('standings_set')
        # TODO DESCOMENTAR
        #     .filter(
        #     betranking__pk__isnull=True
        # ).all()
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championship_current_standings(self) -> List[BetStandings]:
        standings = StandingsModel.objects.filter(championship_table__is_current=True)\
            .order_by("position").select_related().all()

        return list(map(lambda standing: standing.to_domain(), standings))

    def get_current_bet_ranking(self) -> List[Ranking]:
        ranking = BetRanking.objects.filter(championship_table__is_current=True).order_by(
            "-total_points"
        )

        return list(map(lambda bet_ranking: bet_ranking.to_domain(), ranking))

    def get_bet_ranking_by_user(self, user_id: int) -> List[Ranking]:
        ranking = BetRanking.objects.filter(championship_table__is_current=True).filter(user__pk=user_id).order_by(
            "-total_points"
        )

        return ranking.first().to_domain()


class BettorGateway(BettorAdapter):
    def get_bettors_with_active_bets(self):
        bettors = BettorGateway._get_bettor_by_bet_status(BetStatus.ACTIVE.value)
        return list(map(lambda bettor: bettor.to_domain(), bettors))

    @staticmethod
    def _get_bettor_by_bet_status(status: str):
        status = not status
        return User.objects.filter(bet__is_inactive=status).prefetch_related("bet_set").all()


class BetGateway(BetAdapter):
    def get_bet_by_user(self, user_id: int):
        if not user_id:
            raise Exception("Invalid params")

        bets = BetDetails.objects.filter(bet__user_id=user_id)\
            .filter(bet__is_inactive=False).select_related().order_by("position")

        return list(map(lambda bet: bet.to_domain(), bets))

