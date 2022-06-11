from django.db import models

from core.entities import ChampionshipStandingsPosition
from v1.championship.models import ChampionshipTable
from v1.teams.models import Team


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
            team_id=self.team.pk,
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
            last_results=self.last_results,
        )
