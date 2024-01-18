from abc import ABC, abstractmethod
class Reader(ABC):
    @abstractmethod
    def run(self, other: object) -> None:...
