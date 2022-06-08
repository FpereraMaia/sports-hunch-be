from abc import ABC, abstractmethod


class SoccerApiInterface(ABC):
    @abstractmethod
    def get_standings(self):
        return
