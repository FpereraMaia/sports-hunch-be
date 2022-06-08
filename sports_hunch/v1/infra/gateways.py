from django.conf import settings


from core.adapters.gateways import ChampionshipAdapter, BettorAdapter, BetAdapter, StandingsAdapter
from core.entities import Ranking, ChampionshipStandingsPosition, Championship
from typing import List, Dict
from third_party.soccer_api.SoccerApi import SoccerApi
from v1.bet.enums import BetStatus
from v1.bet.models import BetDetails
from v1.championship.models import ChampionshipTable
from v1.ranking.models import BetRanking
from v1.standings.models import Standings
from v1.users.models import User


class ChampionshipGateway(ChampionshipAdapter):
    def update_all(self, attributes):
        ChampionshipTable.objects.filter(is_current=True).update(**attributes)

    def create(self, standings: List[ChampionshipStandingsPosition]) -> Championship:
        championship_table = ChampionshipGateway.assemble_championship_table()
        standings_list = []
        # TODO, E SE DER ERRO AO SALVAR O CAMPEONATO? TEM Q DAR ROLLBACK
        for standing in standings:
            standings_list.append(ChampionshipGateway.assemble_standings(standing, championship_table))
        Standings.objects.bulk_create(standings_list)
        return championship_table.to_domain()

    @staticmethod
    def assemble_championship_table():
        championship_table = ChampionshipTable()
        championship_table.is_current = True
        championship_table.save()
        return championship_table

    @staticmethod
    def assemble_standings(standing: ChampionshipStandingsPosition, championship_table):
        standings_model = Standings()
        standings_model.championship_table = championship_table
        standings_model.team_id = standing.team_id
        standings_model.position = standing.position
        standings_model.points = standing.points
        standings_model.games = standing.games
        standings_model.won = standing.won
        standings_model.drawn = standing.drawn
        standings_model.lost = standing.lost
        standings_model.goal_for = standing.goal_for
        standings_model.goal_against = standing.goal_against
        standings_model.goal_difference = standing.goal_difference
        standings_model.points_percentage = standing.points_percentage
        standings_model.position_variation = standing.position_variation
        standings_model.last_results = standing.last_results
        return standings_model

    def search(self, is_current: bool) -> List[Championship]:
        championships = ChampionshipTable.objects.filter(is_current=is_current).prefetch_related('standings_set')
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championships_without_ranking(self) -> List[Championship]:
        championships = ChampionshipTable.objects.prefetch_related('standings_set').filter(
            betranking__pk__isnull=True
        ).all()
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championship_current_standings(self) -> List[ChampionshipStandingsPosition]:
        standings = Standings.objects.filter(championship_table__is_current=True)\
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
    def _get_bettor_by_bet_status(status: str) -> List[User]:
        status = not status
        return User.objects.filter(bet__is_inactive=status).prefetch_related("bet_set").all()


class BetGateway(BetAdapter):
    def get_bet_by_user(self, user_id: int):
        if not user_id:
            raise Exception("Invalid params")

        bets = BetDetails.objects.filter(bet__user_id=user_id)\
            .filter(bet__is_inactive=False).select_related().order_by("position")

        return list(map(lambda bet: bet.to_domain(), bets))


class StandingsGateway(StandingsAdapter):

    def __init__(self):
        settings_soccer_api = settings.SOCCER_API.get("API_URL")
        championship_id = settings.SOCCER_API.get("BRAZILIAN_CHAMPIONSHIP_ID")
        api_token = settings.SOCCER_API.get("API_TOKEN")
        self.soccer_api = SoccerApi(settings_soccer_api, championship_id, api_token)

    def get_standings(self):
        standings = self.soccer_api.get_standings()
        return StandingsGateway.assemble_list_by_domain(standings)

    @staticmethod
    def assemble_list_by_domain(standings: List):
        return list(map(lambda standing: StandingsGateway.to_domain(standing), standings))

    @staticmethod
    def to_domain(standing: Dict):
        team = standing.get("time")
        return ChampionshipStandingsPosition(
            team_id=team.get("time_id"),
            position=standing.get("posicao"),
            team_name=team.get("nome_popular"),
            team_abbreviation=team.get("sigla"),
            team_crest=team.get("escudo"),
            points=standing.get("pontos"),
            games=standing.get("jogos"),
            won=standing.get("vitorias"),
            drawn=standing.get("empates"),
            lost=standing.get("derrotas"),
            goal_for=standing.get("gols_pro"),
            goal_against=standing.get("gols_contra"),
            goal_difference=standing.get("saldo_gols"),
            points_percentage=standing.get("aproveitamento"),
            position_variation=standing.get("variacao_posicao"),
            last_results=standing.get("ultimos_jogos")
        )
