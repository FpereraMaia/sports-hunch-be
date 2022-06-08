from attrs import asdict

from core.adapters.gateways import BetAdapter


class BetUseCase:
    def __init__(self, bet_gateway: BetAdapter):
        self.bet_gateway = bet_gateway

    def get_bet_standings_by_user(self, user_id: int):
        bets = self.bet_gateway.get_bet_by_user(user_id)
        return list(map(lambda bet: asdict(bet), bets))
