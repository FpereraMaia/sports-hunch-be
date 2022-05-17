from enum import Enum

from bet_details.services import BetDetailsService
from bets.models import Bet
from users.services import UserService


class BetStatus(Enum):
    ACTIVE = True
    INACTIVE = False


class BetService:
    @staticmethod
    def create(user_email, user_name, teams):
        user = UserService.create(user_email, user_name)
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

    @staticmethod
    def _get_bets_by_status(status: bool):
        status_for_filter = not status
        return Bet.objects.filter(is_inactive=status_for_filter).select_related().all()

    @staticmethod
    def get_all_active_bets():
        return BetService._get_bets_by_status(BetStatus.ACTIVE.value)
