from rest_framework import viewsets, status
from rest_framework.response import Response

from core.usecases.bet_usecase import BetUseCase
from core.usecases.championship_usecase import ChampionshipUseCase
from v1.bet.gateways import BetGateway
from v1.championship.gateways import ChampionshipGateway


class BetsDetailsByUserViewSet(viewsets.ViewSet):
    @staticmethod
    def retrieve(request, *args, **kwargs):
        user_id = kwargs.get("pk", None)
        active_bets = BetUseCase(BetGateway()).get_bet_standings_by_user(user_id)
        user_bet_details = ChampionshipUseCase(ChampionshipGateway()).get_bet_ranking_by_user(user_id)
        user_bet_details["bet_standings"] = active_bets
        return Response(user_bet_details, status=status.HTTP_200_OK)
