from rest_framework import serializers

from teams.serializers import TeamSerializer
from v1.ranking.models import Standings


class StandingsModelSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Standings
        fields = "__all__"
