from typing import List

from core.adapters.gateways import ChampionshipAdapter
from core.entities import ChampionshipStandingsPosition, Championship, Ranking
from v1.championship.models import ChampionshipTable
from v1.ranking.models import BetRanking
from v1.standings.models import Standings


class ChampionshipGateway(ChampionshipAdapter):
    def update_all(self, attributes):
        ChampionshipTable.objects.filter(is_current=True).update(**attributes)

    def create(self, standings: List[ChampionshipStandingsPosition]) -> Championship:
        championship_table = ChampionshipGateway.assemble_championship_table()
        standings_list = []
        # TODO, E SE DER ERRO AO SALVAR O CAMPEONATO? TEM Q DAR ROLLBACK
        for standing in standings:
            standings_list.append(
                ChampionshipGateway.assemble_standings(standing, championship_table)
            )
        Standings.objects.bulk_create(standings_list)
        return championship_table.to_domain()

    @staticmethod
    def assemble_championship_table():
        championship_table = ChampionshipTable()
        championship_table.is_current = True
        championship_table.save()
        return championship_table

    @staticmethod
    def assemble_standings(standing: ChampionshipStandingsPosition, championship_table):
        standings_model = Standings()
        standings_model.championship_table = championship_table
        standings_model.team_id = standing.team_id
        standings_model.position = standing.position
        standings_model.points = standing.points
        standings_model.games = standing.games
        standings_model.won = standing.won
        standings_model.drawn = standing.drawn
        standings_model.lost = standing.lost
        standings_model.goal_for = standing.goal_for
        standings_model.goal_against = standing.goal_against
        standings_model.goal_difference = standing.goal_difference
        standings_model.points_percentage = standing.points_percentage
        standings_model.position_variation = standing.position_variation
        standings_model.last_results = standing.last_results
        return standings_model

    def search(self, is_current: bool) -> List[Championship]:
        championships = ChampionshipTable.objects.filter(
            is_current=is_current
        ).prefetch_related("standings_set")
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championships_without_ranking(self) -> List[Championship]:
        championships = (
            ChampionshipTable.objects.prefetch_related("standings_set")
            .filter(betranking__pk__isnull=True)
            .all()
        )
        return list(map(lambda championship: championship.to_domain(), championships))

    def get_championship_current_standings(self) -> List[ChampionshipStandingsPosition]:
        standings = (
            Standings.objects.filter(championship_table__is_current=True)
            .order_by("position")
            .select_related()
            .all()
        )

        return list(map(lambda standing: standing.to_domain(), standings))

    def get_current_bet_ranking(self) -> List[Ranking]:
        ranking = BetRanking.objects.filter(
            championship_table__is_current=True
        ).order_by("-total_points")

        return list(map(lambda bet_ranking: bet_ranking.to_domain(), ranking))
