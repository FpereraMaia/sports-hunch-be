from seed.seed_data.teams import teams_data_seed
from teams.services import TeamService


class Seed:
    @staticmethod
    def seed_teams():
        team_list = []
        for team in teams_data_seed:
            team = TeamService.assemble(team)
            team_list.append(team)

        TeamService.bulk_create(team_list)
        return team_list
