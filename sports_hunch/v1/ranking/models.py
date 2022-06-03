from django.db import models

from core.domains.championship import Championship
from core.entities import ChampionshipStandingsPosition
from teams.models import Team


class ChampionshipTable(models.Model):
    class Meta:
        db_table = "championshiptable"

    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_domain(self):
        standings = list(map(lambda standing: standing.to_domain(), self.standings_set.select_related("team")))
        return Championship(standings)


class Standings(models.Model):
    class Meta:
        db_table = "standings"

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

    def to_domain(self):
        return ChampionshipStandingsPosition(
            position=self.position,
            team_name=self.team.name,
            team_abbreviation=self.team.abbreviation,
            team_crest=self.team.crest,
            points=self.points,
            games=self.games,
            won=self.won,
            drawn=self.drawn,
            lost=self.lost,
            goal_for=self.goal_for,
            goal_against=self.goal_against,
            goal_difference=self.goal_difference,
            points_percentage=self.points_percentage,
            position_variation=self.position_variation,
            last_results=self.last_results
        )
