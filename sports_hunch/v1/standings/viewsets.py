from rest_framework import viewsets, status
from rest_framework.response import Response

from core.usecases.championship_usecase import ChampionshipUseCase
from core.usecases.standing_usecase import StandingUseCase
from v1.infra.gateways import ChampionshipGateway, StandingsGateway
from v1.standings.serializers import StandingsSerializer


class CurrentStandingsViewSet(viewsets.ViewSet):
    @staticmethod
    def list(request, *args, **kwargs):
        standings = ChampionshipUseCase(ChampionshipGateway()).get_current_standings()
        return Response(StandingsSerializer(standings, many=True).data, status=status.HTTP_200_OK)


# class SeedStandingsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     def create(self, request, *args, **kwargs):
#         settings_soccer_api = settings.SOCCER_API.get("API_URL")
#         championship_id = settings.SOCCER_API.get("BRAZILIAN_CHAMPIONSHIP_ID")
#         api_token = settings.SOCCER_API.get("API_TOKEN")
#         soccer_api = SoccerApi(settings_soccer_api, championship_id, api_token)
#         Seed.seed_standings(soccer_api)
#         return Response(status=status.HTTP_201_CREATED)


class CreateStandingsViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request, *args, **kwargs):

        StandingUseCase(StandingsGateway(), ChampionshipGateway()).create_current_standings()
        return Response(status=status.HTTP_201_CREATED)
