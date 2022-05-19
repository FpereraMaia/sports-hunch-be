from bet_details.services import BetDetailsService
from bets.enums import BetStatus
from bets.models import Bet, BetRanking
from seed.models import ChampionshipTable
from users.services import UserService


class BetService:
    @staticmethod
    def create(user_email, user_name, teams):
        user = UserService.create(user_email, user_name)
        BetService.set_inactive(user)
        bet = BetService.assemble(user)
        bet.save()
        try:
            BetDetailsService.create(bet, teams)
        except Exception as err:
            bet.delete()
            raise err

        return {"id": bet.pk, "name": user.name, "email": user.email, "teams": teams}

    @staticmethod
    def assemble(user):
        bet = Bet()
        bet.user = user
        return bet

    @staticmethod
    def set_inactive(user):
        Bet.objects.filter(user_id=user.pk).update(is_inactive=True)

    @staticmethod
    def _get_bets_by_status(status: bool):
        status_for_filter = not status
        return Bet.objects.filter(is_inactive=status_for_filter).select_related().all()

    @staticmethod
    def get_all_active_bets():
        return BetService._get_bets_by_status(BetStatus.ACTIVE.value)

    @staticmethod
    def generate_ranking():
        # TODO isolate entities better. reorganize project
        championship_tables = ChampionshipTable.objects.filter(betranking__pk__isnull=True).all()
        users = UserService.get_users_with_active_bets()
        bet_ranking_list = []
        deitaled_pontuations = []
        for championship_table in championship_tables:
            standings = championship_table.standings_set.all()
            for user in users:
                # pra cada usuário tenhos que pegar as apostas dele em betdetails e calcular em cima da classificação
                user_standings = user.bet_set.filter(is_inactive=False).get().betdetails_set.order_by("position").all()
                total_points, detailed_pontuation = BetService.calculate_points_by_user(standings, user_standings, user.name)
                bet_ranking = BetRanking()
                bet_ranking.user = user
                bet_ranking.championship_table = championship_table
                bet_ranking.total_points = total_points
                bet_ranking_list.append(bet_ranking)
                deitaled_pontuations.append(detailed_pontuation)
        if not bet_ranking_list:
            return
        BetRanking.objects.bulk_create(bet_ranking_list)
        return bet_ranking_list

    @staticmethod
    def calculate_points_by_user(championship_standings, user_standings, user_name):
        # TODO MELHORAR ORGANIZAÇÃO DISSO
        total_points = 0
        detailed_pontuation = []
        for user_standing in user_standings:
            filtered_standing = filter(
                lambda standing: standing.team_id == user_standing.team_id, championship_standings)
            team_position_details = next(filtered_standing, None)

            one_position_above = team_position_details.position + 1
            one_position_below = team_position_details.position - 1
            g6_positions = [x for x in range(1, 7)]
            z4_positions = [x for x in range(17, 21)]
            between_7_and_12_positions = [x for x in range(7, 13)]
            is_in_g6 = (user_standing.position in g6_positions) and (team_position_details.position in g6_positions)
            is_in_z4 = (user_standing.position in z4_positions) and (team_position_details.position in z4_positions)
            between_7_and_12 = (user_standing.position in between_7_and_12_positions) and (team_position_details.position in between_7_and_12_positions)
            dict_log = {
                "team_id": team_position_details.team_id,
                "team_name": team_position_details.team.name,
                "user_name": user_name,
                "user_positinn": user_standing.position,
                "table_position": team_position_details.position,
                "point": 0
            }

            if user_standing.position == team_position_details.position:
                dict_log["point"] = 25
                total_points += 25
                detailed_pontuation.append(dict_log)
                continue
            elif one_position_below <= user_standing.position <= one_position_above:
                dict_log["point"] = 10
                total_points += 10
                detailed_pontuation.append(dict_log)
                continue
            elif is_in_g6 or is_in_z4:
                dict_log["point"] = 6
                total_points += 6
                detailed_pontuation.append(dict_log)
                continue
            elif between_7_and_12:
                dict_log["point"] = 2
                total_points += 2
                detailed_pontuation.append(dict_log)
                continue
        return total_points, detailed_pontuation
