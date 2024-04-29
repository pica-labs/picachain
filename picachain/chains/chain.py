from abc import ABC, abstractmethod


class Chain(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        """execute chain"""
