from abc import ABC, abstractmethod

from core.domains.championship import Championship, BetStandings
from core.entities import Ranking
from typing import List


class ChampionshipAdapter(ABC):
    @abstractmethod
    def get_championships_without_ranking(self) -> List[Championship]:
        pass

    @abstractmethod
    def get_championship_current_standings(self) -> List[BetStandings]:
        pass

    @abstractmethod
    def get_current_bet_ranking(self) -> List[Ranking]:
        pass

    @abstractmethod
    def get_bet_ranking_by_user(self, user_id: int) -> List[Ranking]:
        pass


class BettorAdapter(ABC):
    @abstractmethod
    def get_bettors_with_active_bets(self):
        pass


class BetAdapter(ABC):
    @abstractmethod
    def get_bet_by_user(self, user_id: int):
        pass
