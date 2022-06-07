from attr import define
from typing import List


@define
class Standings:
    position: int
    team_name: str
    team_abbreviation: str
    team_crest: str


@define
class ChampionshipStandingsPosition:
    position: int
    team_name: str
    team_abbreviation: str
    team_crest: str
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
class Bet:
    bettor_id: int
    bettor_name: str
    standings: List[Standings]

    def get_total_points(self, championship_standings):
        pass


@define
class Ranking:
    user_id: int
    user_name: str
    total_points: int
