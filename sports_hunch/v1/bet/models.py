from django.db import models

from core.entities import BetStandings
from v1.teams.models import Team
from v1.users.models import User


class Bet(models.Model):
    class Meta:
        db_table = "bet"
        app_label = "bet"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BetDetails(models.Model):
    class Meta:
        db_table = "betdetails"
        app_label = "bet"

    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_domain(self) -> BetStandings:
        return BetStandings(
            position=self.position,
            team_name=self.team.name,
            team_abbreviation=self.team.abbreviation,
            team_crest=self.team.crest,
            team_id=self.team.team_id,
        )
