from abc import ABC, abstractmethod


class Loader(ABC):
    """Loader Interface"""

    @abstractmethod
    def load(self):
        """Load from path"""
        pass
