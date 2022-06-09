from typing import List, Dict

from django.conf import settings

from core.adapters.gateways import StandingsAdapter
from core.entities import ChampionshipStandingsPosition
from third_party.soccer_api.SoccerApi import SoccerApi


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