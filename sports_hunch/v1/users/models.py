from django.db import models

from core.entities import Bet, Bettor


class User(models.Model):
    class Meta:
        db_table = "user"

    name = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_domain(self) -> Bettor:
        bet_details = self.bet_set.filter(is_inactive=False).get().betdetails_set.order_by("position").all()
        standings = list(map(lambda standing: standing.to_domain(), bet_details))
        bet = Bet(standings=standings)
        return Bettor(id=self.pk, name=self.name, email=self.email, bet=bet)
