from old.seed.interfaces.SoccerApiInterface import SoccerApiInterface
from old.seed.models import ChampionshipTable
from old.seed.seed_data.teams import teams_data_seed
from old.teams.services import TeamService


class Seed:
    @staticmethod
    def seed_teams():
        team_list = []
        for team in teams_data_seed:
            team = TeamService.assemble(team)
            team_list.append(team)

        TeamService.bulk_create(team_list)
        return team_list

    @staticmethod
    def seed_standings(soccer_api: SoccerApiInterface):
        standings = soccer_api.get_standings()
        current_championship = ChampionshipTable.objects.filter(is_current=True)
        if not current_championship.exists():
            return Seed.create_new_championship_table(standings, False)

        championship_current = current_championship.get()
        current_standings = championship_current.standings_set.all()
        standings_is_equal = Seed.verify_api_standings_is_equal_current(
            current_standings, standings
        )

        if not standings_is_equal:
            return Seed.create_new_championship_table(standings)

        return current_standings

    @staticmethod
    def create_new_championship_table(standings, current_championship_exists=True):
        if current_championship_exists:
            ChampionshipTable.objects.filter(is_current=True).update(is_current=False)
        championship_table = Seed.create_championship_table()
        standings_list = []
        for standing in standings:
            standings_list.append(Seed.assemble_standings(standing, championship_table))
        Standings.objects.bulk_create(standings_list)
        return standings_list

    @staticmethod
    def create_championship_table():
        championship_table = ChampionshipTable()
        championship_table.is_current = True
        championship_table.save()
        return championship_table

    @staticmethod
    def assemble_standings(standing, championship_table):
        standings_model = Standings()
        standings_model.championship_table = championship_table
        standings_model.team_id = standing.get("time").get("time_id")
        standings_model.position = standing.get("posicao")
        standings_model.points = standing.get("pontos")
        standings_model.games = standing.get("jogos")
        standings_model.won = standing.get("vitorias")
        standings_model.drawn = standing.get("empates")
        standings_model.lost = standing.get("derrotas")
        standings_model.goal_for = standing.get("gols_pro")
        standings_model.goal_against = standing.get("gols_contra")
        standings_model.goal_difference = standing.get("saldo_gols")
        standings_model.points_percentage = standing.get("aproveitamento")
        standings_model.position_variation = standing.get("variacao_posicao")
        standings_model.last_results = standing.get("ultimos_jogos")
        return standings_model

    @staticmethod
    def verify_api_standings_is_equal_current(current_standings, standings):
        is_equal = True
        for current_standing in current_standings:
            api_standing = list(
                filter(
                    lambda standing: standing.get("time").get("time_id")
                    == current_standing.team_id,
                    standings,
                )
            )

            if api_standing and current_standing.position != api_standing[0].get(
                "posicao"
            ):
                is_equal = False
                break
        return is_equal

    @staticmethod
    def api_standing_is_equal_database_standing(api_standing, current_standing):
        return
