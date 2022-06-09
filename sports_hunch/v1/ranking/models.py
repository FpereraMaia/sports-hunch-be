from django.db import models

from core.entities import Ranking
from v1.championship.models import ChampionshipTable
from v1.users.models import User


class BetRanking(models.Model):
    class Meta:
        db_table = "betranking"

    championship_table = models.ForeignKey(ChampionshipTable, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_points = models.IntegerField()

    def to_domain(self):
        return Ranking(
            user_name=self.user.name,
            total_points=self.total_points,
            user_id=self.user.pk,
            created_at=self.championship_table.created_at
        )
