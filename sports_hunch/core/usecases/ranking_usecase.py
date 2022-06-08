from attrs import asdict

from core.adapters.gateways import ChampionshipAdapter, BettorAdapter


class RankingUseCase:

    def __init__(self, championship_gateway: ChampionshipAdapter, bettor_gateway: BettorAdapter):
        self.championship_gateway = championship_gateway
        self.bettor_gateway = bettor_gateway

    def generate_ranking(self):
        championships = self.championship_gateway.get_championships_without_ranking()
        bettors = self.bettor_gateway.get_bettors_with_active_bets()

        for championship in championships:
            for bettor in bettors:
                total_points = bettor.bet.calculate_total_points(championship)
        return

    def search_current_ranking(self):
        ranking_standing = self.championship_gateway.get_current_bet_ranking()
        return list(map(lambda ranking: asdict(ranking), ranking_standing))
