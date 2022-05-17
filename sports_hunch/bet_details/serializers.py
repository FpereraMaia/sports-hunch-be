from rest_framework import serializers

from teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class BetDetailsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    position = serializers.CharField(max_length=254)
    team = TeamSerializer()
