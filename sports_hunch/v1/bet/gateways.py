from core.adapters.gateways import BetAdapter
from v1.bet.models import BetDetails


class BetGateway(BetAdapter):
    def get_bet_by_user(self, user_id: int):
        if not user_id:
            raise Exception("Invalid params")

        bets = BetDetails.objects.filter(bet__user_id=user_id)\
            .filter(bet__is_inactive=False).select_related().order_by("position")

        return list(map(lambda bet: bet.to_domain(), bets))