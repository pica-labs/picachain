from abc import ABC, abstractmethod
from typing import List

import numpy as np
from PIL.Image import Image

from picachain.embedding import Embedding


class DataStore(ABC):
    """Interface for datastores and vector databases."""

    @abstractmethod
    def create(self):
        """Create a collection for documents and embedding"""

    @abstractmethod
    def add(self, *args, **kwargs):
        """Add embeddings and metadata to collection."""

    @abstractmethod
    def query(self, *args, **kwargs) -> list:
        """similar documents"""

    @abstractmethod
    def delete(self, *args, **kwargs):
        """Delete the collection or index"""
