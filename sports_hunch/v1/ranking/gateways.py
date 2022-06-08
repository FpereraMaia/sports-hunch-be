from typing import List, Dict

from core.adapters.gateways import BetRankingAdapter
from v1.ranking.models import BetRanking


class RankingGateway(BetRankingAdapter):

    def bulk_create_ranking(self, ranking: List[Dict]) -> bool:
        bet_rankings = list(map(lambda bet_ranking: self._assemble_bet_ranking(bet_ranking), ranking))
        BetRanking.objects.bulk_create(bet_rankings)
        return True

    @staticmethod
    def _assemble_bet_ranking(bet_ranking_dict: Dict):
        bet_ranking = BetRanking()
        bet_ranking.user_id = bet_ranking_dict.get("user_id")
        bet_ranking.championship_table_id = bet_ranking_dict.get("championship_id")
        bet_ranking.total_points = bet_ranking_dict.get("total_points")
        return bet_ranking
