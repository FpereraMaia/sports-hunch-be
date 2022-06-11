from attrs import asdict

from core.adapters.gateways import ChampionshipAdapter, BettorAdapter, BetRankingAdapter


class RankingUseCase:
    def __init__(
        self,
        championship_gateway: ChampionshipAdapter,
        bettor_gateway: BettorAdapter,
        bet_ranking_gateway: BetRankingAdapter,
    ):
        self.championship_gateway = championship_gateway
        self.bettor_gateway = bettor_gateway
        self.bet_ranking_gateway = bet_ranking_gateway

    def generate_ranking(self):
        championships = self.championship_gateway.get_championships_without_ranking()
        bettors = self.bettor_gateway.get_bettors_with_active_bets()

        bettor_total_pontuation = []
        for championship in championships:
            for bettor in bettors:
                total_points = bettor.bet.calculate_total_points(championship)
                bettor_total_pontuation.append(
                    {
                        "user_id": bettor.id,
                        "championship_id": championship.id,
                        "total_points": total_points,
                    }
                )

        self.bet_ranking_gateway.bulk_create_ranking(bettor_total_pontuation)

    def search_current_ranking(self):
        ranking_standing = self.championship_gateway.get_current_bet_ranking()
        return list(map(lambda ranking: asdict(ranking), ranking_standing))

    def get_history_by_user(self, user_pk):
        history = self.bet_ranking_gateway.get_ranking_history_by_user(user_pk)
        return list(map(lambda ranking: asdict(ranking), history))

    def get_history(self):
        history = self.bet_ranking_gateway.get_ranking_history()
        return list(map(lambda ranking: asdict(ranking), history))

    def get_bet_ranking_by_user(self, user_id: int):
        bet_ranking = self.bet_ranking_gateway.get_bet_ranking_by_user(user_id)
        return asdict(bet_ranking)
