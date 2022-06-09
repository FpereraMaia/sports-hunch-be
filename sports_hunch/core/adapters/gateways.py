from abc import ABC, abstractmethod

from core.entities import Ranking, ChampionshipStandingsPosition, Championship
from typing import List


class ChampionshipAdapter(ABC):
    @abstractmethod
    def update_all(self, attributes):
        pass

    @abstractmethod
    def create(self, standings: List[ChampionshipStandingsPosition]) -> Championship:
        pass

    @abstractmethod
    def get_championships_without_ranking(self) -> List[Championship]:
        pass

    @abstractmethod
    def get_championship_current_standings(self) -> List[ChampionshipStandingsPosition]:
        pass

    @abstractmethod
    def get_current_bet_ranking(self) -> List[Ranking]:
        pass

    @abstractmethod
    def get_bet_ranking_by_user(self, user_id: int) -> List[Ranking]:
        pass

    @abstractmethod
    def search(self, is_current: bool) -> List[Championship]:
        pass


class BettorAdapter(ABC):
    @abstractmethod
    def get_bettors_with_active_bets(self):
        pass


class BetAdapter(ABC):
    @abstractmethod
    def get_bet_by_user(self, user_id: int):
        pass


class StandingsAdapter(ABC):
    @abstractmethod
    def get_standings(self) -> List[ChampionshipStandingsPosition]:
        pass


class BetRankingAdapter(ABC):
    @abstractmethod
    def bulk_create_ranking(self, ranking: List[dict]) -> bool:
        pass

    @abstractmethod
    def get_ranking_history_by_user(self, user_pk: int):
        pass

    @abstractmethod
    def get_ranking_history(self):
        pass
