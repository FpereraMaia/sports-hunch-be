from bets.enums import BetStatus
from bets.models import BetRanking
from core.adapters.gateways import ChampionshipAdapter, BettorAdapter
from core.domains.championship import Championship, Standings
from core.entities import Ranking
from users.models import User
from v1.ranking.models import ChampionshipTable, Standings as StandingsModel


class ChampionshipGateway(ChampionshipAdapter):
    def get_championships_without_ranking(self) -> list[Championship]:
        championships = ChampionshipTable.objects.prefetch_related('standings_set')
        # TODO DESCOMENTAR
        #     .filter(
        #     betranking__pk__isnull=True
        # ).all()
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championship_current_standings(self) -> list[Standings]:
        standings = StandingsModel.objects.filter(championship_table__is_current=True)\
            .order_by("position").select_related().all()

        return list(map(lambda standing: standing.to_domain(), standings))

    def get_current_bet_ranking(self) -> list[Ranking]:
        ranking = BetRanking.objects.filter(championship_table__is_current=True).order_by(
            "-total_points"
        )

        return list(map(lambda bet_ranking: bet_ranking.to_domain(), ranking))


class BettorGateway(BettorAdapter):
    def get_bettors_with_active_bets(self):
        bettors = BettorGateway._get_bettor_by_bet_status(BetStatus.ACTIVE.value)
        return list(map(lambda bettor: bettor.to_domain(), bettors))

    @staticmethod
    def _get_bettor_by_bet_status(status: str):
        status = not status
        return User.objects.filter(bet__is_inactive=status).prefetch_related("bet_set").all()
