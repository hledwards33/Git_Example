from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def run(self, name: str):
        pass
