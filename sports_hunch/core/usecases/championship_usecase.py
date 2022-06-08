from attrs import asdict

from core.adapters.gateways import ChampionshipAdapter


class ChampionshipUseCase:

    def __init__(self, championship_gateway: ChampionshipAdapter):
        self.championship_gateway = championship_gateway

    def get_current_standings(self):
        standings = self.championship_gateway.get_championship_current_standings()
        return list(map(lambda standing: asdict(standing), standings))

    def get_bet_ranking_by_user(self, user_id: int):
        bet_ranking = self.championship_gateway.get_bet_ranking_by_user(user_id)
        return asdict(bet_ranking)
