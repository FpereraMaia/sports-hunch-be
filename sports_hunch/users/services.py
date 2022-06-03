from bets.enums import BetStatus
from users.models import User


class UserService:
    @staticmethod
    def create(email, name):
        user = UserService.assemble(email, name)
        user.save()
        return user

    @staticmethod
    def assemble(email, name):
        try:
            user = User.objects.get(email__icontains=email)
        except User.DoesNotExist:
            user = User()
            user.email = email

        user.name = name
        return user

    @staticmethod
    def get_users_with_active_bets():
        return UserService._get_users_by_bet_status(BetStatus.ACTIVE.value)

    @staticmethod
    def _get_users_by_bet_status(status: str):
        status = not status
        return User.objects.filter(bet__is_inactive=status).all()
