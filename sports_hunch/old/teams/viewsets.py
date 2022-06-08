from rest_framework import viewsets

from old.teams.models import Team
from old.teams.serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
