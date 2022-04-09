from bet_details.models import BetDetails
from teams.services import TeamService


class BetDetailsService:
    @staticmethod
    def create(bet, teams):
        bet_details_list = []
        for index_ in range(len(teams)):
            team = teams[index_]
            team_position = index_ + 1
            bet_details = BetDetailsService.assemble(bet, team.get("team_id"), team_position)
            bet_details_list.append(bet_details)

        BetDetails.objects.bulk_create(bet_details_list)

    @staticmethod
    def assemble(bet, team_id, position):
        bet_details = BetDetails()
        bet_details.bet = bet
        bet_details.team = TeamService.get_by_id(team_id)
        bet_details.position = position
        return bet_details
