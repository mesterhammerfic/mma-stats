import abc
import dataclasses
from typing import List


@dataclasses.dataclass
class Fighter:
    id: int
    name: str


class DataModel(abc.ABC):
    @abc.abstractmethod
    def close(self) -> None:
        """
        closes the connection to the database
        """
        ...

    @abc.abstractmethod
    def get_fighters(self) -> List[Fighter]:
        """
        :return: list of fighters
        """
        ...


class TestDataModel(DataModel):
    def close(self) -> None:
        pass

    def get_fighters(self) -> List[Fighter]:
        return [
            Fighter(1, "Ronaldo Souza"),
            Fighter(2, "Roger Gracie"),
            Fighter(3, "Rafael Lovato Jr."),
        ]
