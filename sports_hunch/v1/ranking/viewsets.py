from rest_framework import status, viewsets
from rest_framework.response import Response

from core.usecases.ranking_usecase import RankingUseCases
from v1.gateways import ChampionshipGateway, BettorGateway


class GenerateRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request, *args, **kwargs):
        RankingUseCases(ChampionshipGateway(), BettorGateway()).generate_ranking()
        return Response(status=status.HTTP_201_CREATED)


class CurrentRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request, *args, **kwargs):
        ranking_standings = RankingUseCases(ChampionshipGateway(), BettorGateway()).search_current_ranking()
        return Response(ranking_standings, status=status.HTTP_200_OK)
