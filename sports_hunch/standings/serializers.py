from rest_framework import serializers

from seed.models import Standings
from teams.serializers import TeamSerializer


class StandingsModelSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Standings
        fields = "__all__"
