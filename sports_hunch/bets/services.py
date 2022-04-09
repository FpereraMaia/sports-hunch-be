from bet_details.services import BetDetailsService
from bets.models import Bet
from users.services import UserService


class BetService:
    @staticmethod
    def create(user_name, user_email, teams):
        user = UserService.create(user_name, user_email)
        BetService.set_inactive(user)
        bet = BetService.assemble(user)
        bet.save()
        try:
            BetDetailsService.create(bet, teams)
        except Exception as err:
            bet.delete()
            raise err

        return {
            "id": bet.pk,
            "name": user.name,
            "email": user.email,
            "teams": teams
        }

    @staticmethod
    def assemble(user):
        bet = Bet()
        bet.user = user
        return bet

    @staticmethod
    def set_inactive(user):
        Bet.objects.filter(user_id=user.pk).update(is_inactive=True)
