from teams.models import Team


class TeamService:
    @staticmethod
    def get_by_id(team_id):
        return Team.objects.get(pk=team_id)

    @staticmethod
    def assemble(data):
        team = Team(**data)
        return team

    @staticmethod
    def bulk_create(team_list):
        Team.objects.bulk_create(team_list)