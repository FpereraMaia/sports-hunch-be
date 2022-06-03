from django.db import models

from core.entities import Ranking
from seed.models import ChampionshipTable
from users.models import User


class Bet(models.Model):
    class Meta:
        db_table = "bet"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_inactive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BetRanking(models.Model):
    class Meta:
        db_table = "betranking"

    championship_table = models.ForeignKey(ChampionshipTable, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField()

    def to_domain(self):
        return Ranking(user_name=self.user.name, total_points=self.total_points, user_id=self.user.pk)
