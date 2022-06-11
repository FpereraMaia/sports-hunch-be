from rest_framework import viewsets, status
from rest_framework.response import Response

from core.usecases.championship_usecase import ChampionshipUseCase
from core.usecases.standing_usecase import StandingUseCase
from v1.championship.gateways import ChampionshipGateway
from v1.standings.gateways import StandingsGateway

from v1.standings.serializers import StandingsSerializer


class CurrentStandingsViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request, *args, **kwargs):
        standings = ChampionshipUseCase(ChampionshipGateway()).get_current_standings()
        return Response(
            StandingsSerializer(standings, many=True).data, status=status.HTTP_200_OK
        )


class CreateStandingsViewSet(viewsets.ViewSet):
    @staticmethod
    def create(request, *args, **kwargs):

        StandingUseCase(
            StandingsGateway(), ChampionshipGateway()
        ).create_current_standings()
        return Response(status=status.HTTP_201_CREATED)
