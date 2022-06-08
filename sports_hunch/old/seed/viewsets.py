from django.conf import settings

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from old.bets import BetService
from old.seed.services import Seed
from third_party.soccer_api.SoccerApi import SoccerApi
from old.teams.serializers import TeamSeedSerializer


class SportsHunchViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        teams = Seed.seed_teams()
        return Response(
            TeamSeedSerializer(teams, many=True).data, status=status.HTTP_201_CREATED
        )


class SeedStandingsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        settings_soccer_api = settings.SOCCER_API.get("API_URL")
        championship_id = settings.SOCCER_API.get("BRAZILIAN_CHAMPIONSHIP_ID")
        api_token = settings.SOCCER_API.get("API_TOKEN")
        soccer_api = SoccerApi(settings_soccer_api, championship_id, api_token)
        Seed.seed_standings(soccer_api)
        return Response(status=status.HTTP_201_CREATED)


class SeedBetRankingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        BetService.generate_ranking()
        return Response(status=status.HTTP_201_CREATED)
