from rest_framework import serializers


class StandingsSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    team_name = serializers.CharField()
    team_abbreviation = serializers.CharField()
    team_crest = serializers.CharField()
    points = serializers.IntegerField()
    games = serializers.IntegerField()
    won = serializers.IntegerField()
    drawn = serializers.IntegerField()
    lost = serializers.IntegerField()
    goal_for = serializers.IntegerField()
    goal_against = serializers.IntegerField()
    goal_difference = serializers.IntegerField()
    points_percentage = serializers.IntegerField()
    position_variation = serializers.IntegerField()
    last_results = serializers.CharField()
