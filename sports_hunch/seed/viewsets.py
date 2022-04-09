from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from seed.services import Seed
from teams.serializers import TeamSeedSerializer


class SportsHunchViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    def create(self, request, *args, **kwargs):
        teams = Seed.seed_teams()
        return Response(TeamSeedSerializer(teams, many=True).data, status=status.HTTP_201_CREATED)
