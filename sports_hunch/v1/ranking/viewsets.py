from rest_framework import status, viewsets
from rest_framework.response import Response

from core.usecases.ranking_usecase import RankingUseCase
from v1.infra.gateways import ChampionshipGateway, BettorGateway
from v1.ranking.gateways import RankingGateway


class GenerateRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request, *args, **kwargs):
        RankingUseCase(ChampionshipGateway(), BettorGateway(), RankingGateway()).generate_ranking()
        return Response(status=status.HTTP_201_CREATED)


class CurrentRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request, *args, **kwargs):
        ranking_standings = RankingUseCase(ChampionshipGateway(), BettorGateway()).search_current_ranking()
        return Response(ranking_standings, status=status.HTTP_200_OK)
