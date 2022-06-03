from rest_framework import mixins, viewsets
from rest_framework.response import Response

from bet_details.models import BetDetails
from bet_details.serializers import BetDetailsListSerializer
from bet_details.services import BetDetailsService


class BetsDetailsByUserViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = BetDetails.objects.all()

    @staticmethod
    def retrieve(request, *args, **kwargs):
        user_id = kwargs.get("pk", None)
        active_bets = BetDetailsService.get_standings_by_user(user_id)
        serializer = BetDetailsListSerializer(active_bets, many=True)
        return Response(serializer.data)
