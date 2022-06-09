from rest_framework import status, viewsets
from rest_framework.response import Response

from core.usecases.ranking_usecase import RankingUseCase
from v1.ranking.gateways import RankingGateway


class GenerateRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def create(request, *args, **kwargs):
        RankingUseCase(ChampionshipGateway(), BettorGateway(), RankingGateway()).generate_ranking()
        return Response(status=status.HTTP_201_CREATED)


class CurrentRankingViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request, *args, **kwargs):
        ranking_standings = RankingUseCase(
            ChampionshipGateway(), BettorGateway(), RankingGateway()).search_current_ranking()

        return Response(ranking_standings, status=status.HTTP_200_OK)


class RankingHistoryViewSet(viewsets.ViewSet):

    @staticmethod
    def retrieve(request, *args, **kwargs):
        user_pk = kwargs.get("pk")
        ranking_history_by_user = RankingUseCase(
            ChampionshipGateway(), BettorGateway(), RankingGateway()).get_history_by_user(user_pk)

        return Response(ranking_history_by_user, status=status.HTTP_200_OK)

    @staticmethod
    def list(request, *args, **kwargs):
        ranking_history = RankingUseCase(
            ChampionshipGateway(), BettorGateway(), RankingGateway()).get_history()

        history_response = RankingHistoryViewSet._get_list_response(ranking_history)
        return Response(history_response, status=status.HTTP_200_OK)

    @staticmethod
    def _get_list_response(rankings):
        response = {}
        for ranking in rankings:
            created_date = ranking.get("created_at")
            created_date = created_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z')

            if created_date in response:
                response[created_date].append(ranking)
                continue
            response[created_date] = [ranking]

        return response
