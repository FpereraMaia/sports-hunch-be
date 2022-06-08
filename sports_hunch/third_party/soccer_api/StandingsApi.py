import requests
from requests.structures import CaseInsensitiveDict


class StandingsApi:
    def __init__(self, api_url, championship_id, token):
        self.api_url = api_url
        self.standings_url = "{}/campeonatos/{}/tabela".format(api_url, championship_id)
        self.token = token

    def get_standings(self):
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {token}".format(token=self.token)
        standings = requests.get(self.standings_url, headers=headers)
        standings.raise_for_status()
        return standings.json()
