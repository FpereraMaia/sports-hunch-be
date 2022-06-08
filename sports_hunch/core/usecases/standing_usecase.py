from core.adapters.gateways import StandingsAdapter, ChampionshipAdapter


class StandingUseCase:
    def __init__(self, standings_gateway: StandingsAdapter, championship_gateway: ChampionshipAdapter):
        self.standings_gateway = standings_gateway
        self.championship_gateway = championship_gateway
    
    def create_current_standings(self):
        standings = self.standings_gateway.get_standings()
        championships = self.championship_gateway.search(True)

        if not championships:
            return self.championship_gateway.create(standings)

        championship = championships[0]

        is_equal = championship.compare_championship_standings(standings)
        if not is_equal:
            self.championship_gateway.update_all({"is_current": False})
            return self.championship_gateway.create(standings)

        return championship.standings



        #
        # championship_current = current_championship.get()
        # current_standings = championship_current.standings_set.all()
        # standings_is_equal = Seed.verify_api_standings_is_equal_current(
        #     current_standings, standings
        # )
        #
        # if not standings_is_equal:
        #     return Seed.create_new_championship_table(standings)
        #
        # return current_standings
