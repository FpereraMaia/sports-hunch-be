from rest_framework import routers

from v1.ranking.viewsets import GenerateRankingViewSet, CurrentRankingViewSet
from v1.standings.viewsets import CurrentStandingsViewSet

router = routers.DefaultRouter()
router.register(r'championship/id/bets/type/ranking', GenerateRankingViewSet, basename="GenerateRanking")
router.register(r"championship/standings/current", CurrentStandingsViewSet, basename="CurrentStandingViewSet")
router.register(r"bet/ranking", CurrentRankingViewSet, basename="CurrentStandingViewSet")

