from django.db import models


class Team(models.Model):
    class Meta:
        db_table = "team"

    team_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=45)
    abbreviation = models.CharField(max_length=5)
    crest = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
