from attr import define

from core.interfaces.chain_of_responsability import AbstractHandler


@define
class BetAndChampionshipPositionsAggregator:
    bet_position: int
    championship_team_position: int


class EqualPositionsHandler(AbstractHandler):
    POINTS_EARNED = 25

    def handle(self, request: BetAndChampionshipPositionsAggregator) -> int:
        if request.bet_position == request.championship_team_position:
            return self.POINTS_EARNED
        else:
            return super().handle(request)


class OnePositionBelowOrAbove(AbstractHandler):
    POINTS_EARNED = 10

    def handle(self, request: BetAndChampionshipPositionsAggregator) -> int:
        one_position_above = request.championship_team_position + 1
        one_position_below = request.championship_team_position - 1

        if one_position_below <= request.bet_position <= one_position_above:
            return self.POINTS_EARNED
        else:
            return super().handle(request)


class IsInG6orG4Positions(AbstractHandler):
    POINTS_EARNED = 6
    G6_POSITIONS = [x for x in range(1, 7)]
    Z4_POSITIONS = [x for x in range(17, 21)]

    def handle(self, request: BetAndChampionshipPositionsAggregator) -> int:
        is_in_g6 = (request.bet_position in self.G6_POSITIONS) and (
                request.championship_team_position in self.G6_POSITIONS
        )
        is_in_z4 = (request.bet_position in self.Z4_POSITIONS) and (
                request.championship_team_position in self.Z4_POSITIONS
        )

        if is_in_g6 or is_in_z4:
            return self.POINTS_EARNED
        else:
            return super().handle(request)


class IsBetween7and12Positions(AbstractHandler):
    POINTS_EARNED = 2
    POSITIONS_7_TO_12 = [x for x in range(7, 13)]

    def handle(self, request: BetAndChampionshipPositionsAggregator) -> int:
        between_7_and_12 = (request.bet_position in self.POSITIONS_7_TO_12) \
                           and (request.championship_team_position in self.POSITIONS_7_TO_12)

        if between_7_and_12:
            return self.POINTS_EARNED
        else:
            return super().handle(request)


class CalculateRankingPoints:
    @staticmethod
    def calculate(championship_team_position: int, bet_team_position: int):
        equals_position = EqualPositionsHandler()
        one_position_below_or_above = OnePositionBelowOrAbove()
        is_in_g6_or_z4 = IsInG6orG4Positions()
        is_between_7_and_12 = IsBetween7and12Positions()

        equals_position.set_next(one_position_below_or_above).set_next(is_in_g6_or_z4).set_next(is_between_7_and_12)

        positions = BetAndChampionshipPositionsAggregator(
            championship_team_position=championship_team_position, bet_position=bet_team_position)

        return equals_position.handle(positions)

