from abc import ABC, abstractmethod

from core.domains.championship import Championship, Standings
from core.entities import Ranking


class ChampionshipAdapter(ABC):
    @abstractmethod
    def get_championships_without_ranking(self) -> list[Championship]:
        pass

    @abstractmethod
    def get_championship_current_standings(self) -> list[Standings]:
        pass

    @abstractmethod
    def get_current_bet_ranking(self) -> list[Ranking]:
        pass


class BettorAdapter(ABC):
    @abstractmethod
    def get_bettors_with_active_bets(self):
        pass
