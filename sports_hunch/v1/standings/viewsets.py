
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.usecases.championship_usecase import ChampionshipUsecase
from v1.gateways import ChampionshipGateway
from v1.standings.serializers import StandingsSerializer


class CurrentStandingsViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request, *args, **kwargs):
        standings = ChampionshipUsecase(ChampionshipGateway()).get_current_standings()
        return Response(StandingsSerializer(standings, many=True).data, status=status.HTTP_200_OK)
