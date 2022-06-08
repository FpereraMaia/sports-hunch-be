from django.db import models

from core.entities import Championship


class ChampionshipTable(models.Model):
    class Meta:
        db_table = "championshiptable"

    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_domain(self):
        standings = list(map(lambda standing: standing.to_domain(), self.standings_set.select_related("team")))
        return Championship(standings)
