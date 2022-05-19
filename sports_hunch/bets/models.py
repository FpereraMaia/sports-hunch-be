from django.db import models

from seed.models import ChampionshipTable
from users.models import User


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BetRanking(models.Model):
    championship_table = models.ForeignKey(ChampionshipTable, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField()
