from typing import List

from core.adapters.gateways import BettorAdapter
from v1.bet.enums import BetStatus
from v1.users.models import User


class BettorGateway(BettorAdapter):
    def get_bettors_with_active_bets(self):
        bettors = BettorGateway._get_bettor_by_bet_status(BetStatus.ACTIVE.value)
        return list(map(lambda bettor: bettor.to_domain(), bettors))

    @staticmethod
    def _get_bettor_by_bet_status(status: str) -> List[User]:
        status = not status
        return (
            User.objects.filter(bet__is_inactive=status)
            .prefetch_related("bet_set")
            .all()
        )
