from rest_framework import serializers

from teams.serializers import TeamSerializer


class BetPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=254)
    email = serializers.EmailField()
    teams = TeamSerializer(many=True)
