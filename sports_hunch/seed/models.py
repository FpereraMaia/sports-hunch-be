from django.db import models

from teams.models import Team


class ChampionshipTable(models.Model):
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Standings(models.Model):
    championship_table = models.ForeignKey(ChampionshipTable, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.IntegerField()
    games = models.IntegerField()
    won = models.IntegerField()
    drawn = models.IntegerField()
    lost = models.IntegerField()
    goal_for = models.IntegerField()
    goal_against = models.IntegerField()
    goal_difference = models.IntegerField()
    points_percentage = models.FloatField()
    position_variation = models.IntegerField()
    last_results = models.CharField(max_length=45)
