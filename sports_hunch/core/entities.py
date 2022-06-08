from attr import define
from typing import List


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
    bettor_id: int
    bettor_name: str
    standings: List[BetStandings]

    def get_total_points(self, championship_standings):
        pass


@define
class Ranking:
    user_id: int
    user_name: str
    total_points: int


@define
class Bettor:
    name: str
    email: str
    bet: Bet
