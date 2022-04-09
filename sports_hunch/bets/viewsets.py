from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from bets.serializers import BetPostSerializer
from bets.services import BetService


class BetsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = BetPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        reponse = BetService.create(data.get("email"), data.get("name"), data.get("teams"))
        headers = self.get_success_headers(serializer.data)

        return Response(reponse, status=status.HTTP_201_CREATED, headers=headers)
