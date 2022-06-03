from django.db import models

from bets.models import Bet
from core.domains.championship import BetStandings
from teams.models import Team


class BetDetails(models.Model):
    class Meta:
        db_table = "betdetails"

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
            team_id=self.team.team_id
        )
