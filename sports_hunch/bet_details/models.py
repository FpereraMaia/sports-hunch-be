from django.db import models

from bets.models import Bet
from teams.models import Team


class BetDetails(models.Model):
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)