from rest_framework import serializers

from teams.models import Team


class TeamSeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["team_id", "name", "abbreviation", "crest"]


class TeamSerializer(TeamSeedSerializer):
    team_id = serializers.IntegerField()
