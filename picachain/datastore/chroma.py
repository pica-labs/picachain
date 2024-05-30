__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")


import uuid
from collections import defaultdict
from typing import Any, List

import chromadb
import numpy as np
from chromadb import Collection
from PIL.Image import Image
from tqdm import tqdm

from picachain.datastore.base import DataStore
from picachain.structures import Document
from picachain.utils.image_util import base64_to_image, image_to_base64


class ChromaStore(DataStore):
    """Chroma DB class"""

    collection_index: Collection

    def __init__(
        self,
        storage_path: str = "./chroma",
        metadata: dict = {"hnsw:space": "cosine"},
    ) -> None:
        """
        - storage_path (str)
        - database
        - metadata(dict): available options for 'hnsw:space' are 'l2', 'ip' or 'cosine'.
        """

        self.metadata = metadata

        self.client = chromadb.PersistentClient(
            path=storage_path,
        )

    def health_check(self) -> bool:
        return isinstance(self.client.heartbeat(), int)

    def list_collections(self) -> List[str]:
        """Get the list of created collections."""
        return [col.name for col in self.client.list_collections()]

    def create(self, collection_name: str) -> Collection:
        """Create data collection

        Returns:
        - success (bool)
        """
        try:
            self.collection_index = self.client.get_or_create_collection(
                name=collection_name,
                metadata=self.metadata,
            )
            return True
        except Exception as e:
            raise KeyError(f"Collection {self.collection_name} not found: {e}")

    def _proces_documents(self, documents: List[Document]):
        return [
            Document(content=image_to_base64(doc.content), metadata=doc.metadata)
            for doc in documents
        ]

    def add(
        self,
        documents: List[Document],
        embeddings: List[float],
    ):
        """Ingest documents to database.

        Args:
        - documents(list): list of documents to be added.
        - embeddings (list): embeddings for respective document

        Returns:
        - success (bool)
        """
        try:
            _ids = []
            _documents = []
            _metadatas = []
            for doc in tqdm(documents, desc="Adding documents"):
                _ids.append(doc.metadata["id"])
                _metadatas.append(doc.metadata)
                _documents.append(doc.content)

            self.collection_index.add(
                embeddings=embeddings,
                ids=_ids,
                documents=_documents,
                metadatas=_metadatas,
            )
            return True
        except Exception as e:
            raise Exception(f"Failed to add documents to Chroma store. {e}")

    def query(
        self,
        query_embedding: List[float],
        top_k: int = 3,
    ) -> list:
        """Retrieve relevant documents from chroma database

        Args:
        - collection: created collection
        - query_embedding: query document embedding
        - top_k (int): top k documents to retrieve

        Returns:
        - relevant documents
        """
        try:
            result = self.collection_index.query(
                query_embeddings=query_embedding,
                n_results=top_k,
            )
            return result
        except Exception as e:
            raise FileNotFoundError(f"Failed to query relevant results. {e}")

    def delete(self, collection_name: str):
        if collection_name not in self.list_collections():
            return f"No collection found with name: {collection_name}"
        else:
            self.client.delete_collection(collection_name)
            return True

    @property
    def collection(self):
        info = defaultdict(str)
        info["name"] = self.collection_index.name
        info["count"] = self.collection_index.count()
        info["top_10_items"] = self.collection_index.peek()
        return info
