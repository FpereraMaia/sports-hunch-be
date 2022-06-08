from attr import define
from typing import List

from core.utils.calculate_ranking_points import CalculateRankingPoints


@define
class BetStandings:
    position: int
    team_name: str
    team_abbreviation: str
    team_crest: str
    team_id: int


@define
class ChampionshipStandingsPosition:
    position: int
    team_name: str
    team_abbreviation: str
    team_crest: str
    team_id: int
    points: int
    games: int
    won: int
    drawn: int
    lost: int
    goal_for: int
    goal_against: int
    goal_difference: int
    points_percentage: int
    position_variation: int
    last_results: str


@define
class Championship:
    id: int
    standings: List[ChampionshipStandingsPosition]

    def compare_championship_standings(self, standings_to_compare: List[ChampionshipStandingsPosition]):
        is_equal = True
        for current_standing in self.standings:
            standings = list(
                filter(
                    lambda standing: standing.team_id
                    == current_standing.team_id,
                    standings_to_compare,
                )
            )

            if standings and current_standing.position != standings[0].position:
                is_equal = False
                break
        return is_equal


@define
class Bet:
    standings: List[BetStandings]

    def calculate_total_points(self, championship: Championship):
        total_points = 0
        for bet_standing in self.standings:
            filtered_standing = filter(
                lambda standing: standing.team_id == bet_standing.team_id,
                championship.standings,
            )
            team_position_details = next(filtered_standing, None)

            points = CalculateRankingPoints.calculate(team_position_details.position, bet_standing.position)
            if points:
                total_points += points

        return total_points


@define
class Ranking:
    user_id: int
    user_name: str
    total_points: int


@define
class Bettor:
    id: int
    name: str
    email: str
    bet: Bet
