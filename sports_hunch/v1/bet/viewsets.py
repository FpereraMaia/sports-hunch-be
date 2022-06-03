from rest_framework import viewsets, status
from rest_framework.response import Response

from core.usecases.bet_usecase import BetUseCase
from core.usecases.championship_usecase import ChampionshipUsecase
from v1.gateways import BetGateway, ChampionshipGateway


class BetsDetailsByUserViewSet(viewsets.ViewSet):
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get("pk", None)
        active_bets = BetUseCase(BetGateway()).get_championship_current_standings(user_id)
        return Response(active_bets, status=status.HTTP_200_OK)


class BetDetailsUserRankingViewSet(viewsets.ViewSet):
    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get("pk", None)
        active_bets = ChampionshipUsecase(ChampionshipGateway()).get_bet_ranking_by_user(user_id)
        return Response(active_bets, status=status.HTTP_200_OK)
