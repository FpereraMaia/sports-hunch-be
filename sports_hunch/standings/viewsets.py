from rest_framework import mixins, viewsets

from seed.models import Standings
from standings.serializers import StandingsModelSerializer


class CurrentStandingsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Standings.objects.filter(championship_table__is_current=True).order_by("position").select_related().all()
    serializer_class = StandingsModelSerializer
