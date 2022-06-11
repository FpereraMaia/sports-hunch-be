from typing import List, Dict

from core.adapters.gateways import BetRankingAdapter
from core.entities import Ranking
from v1.ranking.models import BetRanking


class RankingGateway(BetRankingAdapter):
    def bulk_create_ranking(self, ranking: List[Dict]) -> bool:
        bet_rankings = list(
            map(lambda bet_ranking: self._assemble_bet_ranking(bet_ranking), ranking)
        )
        BetRanking.objects.bulk_create(bet_rankings)
        return True

    def get_ranking_history_by_user(self, user_pk):
        bet_rankings = (
            BetRanking.objects.select_related("championship_table")
            .filter(user_id=user_pk)
            .order_by("championship_table__created_at")
            .all()
        )

        return list(map(lambda bet_ranking: bet_ranking.to_domain(), bet_rankings))

    def get_ranking_history(self):
        bet_rankings = (
            BetRanking.objects.select_related("championship_table")
            .order_by("championship_table__created_at", "-total_points")
            .all()
        )

        return list(map(lambda bet_ranking: bet_ranking.to_domain(), bet_rankings))

    def get_bet_ranking_by_user(self, user_id: int) -> List[Ranking]:
        ranking = (
            BetRanking.objects.filter(championship_table__is_current=True)
            .filter(user__pk=user_id)
            .order_by("-total_points")
        )

        return ranking.first().to_domain()

    @staticmethod
    def _assemble_bet_ranking(bet_ranking_dict: Dict):
        bet_ranking = BetRanking()
        bet_ranking.user_id = bet_ranking_dict.get("user_id")
        bet_ranking.championship_table_id = bet_ranking_dict.get("championship_id")
        bet_ranking.total_points = bet_ranking_dict.get("total_points")
        return bet_ranking
