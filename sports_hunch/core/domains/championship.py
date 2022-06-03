from attr import define, field


@define
class BetStandings:
    position: int
    team_name: str
    team_abbreviation: str
    team_crest: str
    team_id: int


@define
class Championship:
    standings: list[BetStandings]


@define
class Bet:
    standings: list[BetStandings]
    rules = {
        "exact"
        "is_in_g6": {
            "operator": [x for x in range(1, 7)],
            "points": 6
        }
    }
    _g6_positions: list = field(init=False, default=[x for x in range(1, 7)])
    _z4_positions: list = field(init=False, default=[x for x in range(17, 21)])
    _between_7_and_12_positions = [x for x in range(7, 13)]

    def calculate_total_points(self, championship: Championship):
        for bet_standing in self.standings:
            filtered_standing = filter(
                lambda standing: standing.team_id == bet_standing.team_id,
                championship.standings,
            )
            team_position_details = next(filtered_standing, None)
        pass


@define
class Bettor:
    name: str
    email: str
    bet: Bet
