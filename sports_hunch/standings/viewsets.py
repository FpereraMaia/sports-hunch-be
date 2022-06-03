from rest_framework import mixins, viewsets

from standings.serializers import StandingsModelSerializer
from v1.ranking.models import Standings


class CurrentStandingsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = (
        Standings.objects.filter(championship_table__is_current=True)
        .order_by("position")
        .select_related()
        .all()
    )
    serializer_class = StandingsModelSerializer
