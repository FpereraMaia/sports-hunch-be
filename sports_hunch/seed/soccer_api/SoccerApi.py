from seed.interfaces.SoccerApiInterface import SoccerApiInterface
from seed.soccer_api.StandingsApi import StandingsApi


class SoccerApi(SoccerApiInterface):
    def __init__(self, api_url, championship_id, token):
        self.standings_service = StandingsApi(api_url, championship_id, token)

    def get_standings(self):
        return self.standings_service.get_standings()

