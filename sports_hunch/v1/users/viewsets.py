from rest_framework import mixins, viewsets

from old.users.serializers import ActiveUsersListSerializer
from v1.users.models import User


class ActiveUsersListViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.filter(bet__is_inactive=False).all()
    serializer_class = ActiveUsersListSerializer
