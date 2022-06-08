from rest_framework import serializers

from old.seed.models import ChampionshipTable
from old.teams.serializers import TeamSerializer
from old.users.serializers import ActiveUsersListSerializer


class BetPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=254)
    email = serializers.EmailField()
    teams = TeamSerializer(many=True)


class ChampionshipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionshipTable
        fields = "__all__"


class CurrentRankingSerializer(serializers.Serializer):
    total_points = serializers.IntegerField()
    championship_table = ChampionshipModelSerializer()
    user = ActiveUsersListSerializer()