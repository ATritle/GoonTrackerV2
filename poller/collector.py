from abc import ABC, abstractmethod


class Collector(ABC):

    @abstractmethod
    def poll(self):
        pass