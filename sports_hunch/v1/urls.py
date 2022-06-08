from rest_framework import routers

from v1.bet.viewsets import BetsDetailsByUserViewSet
from v1.ranking.viewsets import GenerateRankingViewSet, CurrentRankingViewSet
from v1.standings.viewsets import CurrentStandingsViewSet, CreateStandingsViewSet

router = routers.DefaultRouter()
router.register(r'championship/id/bets/type/ranking', GenerateRankingViewSet, basename="GenerateRanking")
router.register(r'championship/standings', CreateStandingsViewSet, basename="GenerateRanking")


router.register(r"championship/standings/current", CurrentStandingsViewSet, basename="CurrentStandingsViewSet")
router.register(r"bet/ranking", CurrentRankingViewSet, basename="CurrentRankingViewSet")
router.register(r"bet/details/user", BetsDetailsByUserViewSet, basename="BetsDetailsByUserViewSet")
