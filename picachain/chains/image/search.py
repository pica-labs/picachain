from typing import Any, List, Union

from PIL import Image

from picachain.datastore import DataStore
from picachain.embedding import ClipEmbedding, Embedding
from picachain.retriever import ImageRetriever


class ImageSearchChain:
    query: Union[Image.Image, str]
    datastore: DataStore
    embedding: Union[Embedding, ClipEmbedding]
    top_k: int = 3

    def _encode_query_image(self, image: Union[Image.Image, List[float]]):
        query_embedding = None
        if isinstance(image, Image.Image):
            query_embedding = self.embedding.encode_images([image])
        if isinstance(image, float):
            query_embedding = image
        return query_embedding

    @classmethod
    def from_image(
        cls,
        image: Image.Image,
        datastore: DataStore,
        embedding: Union[Embedding, ClipEmbedding],
        top_k: int = 3,
    ):
        return cls(
            query=image,
            datastore=datastore,
            embedding=embedding,
            top_k=top_k,
        )

    def run(self):
        try:
            _query_embedding = self._encode_query_image(self.query)
            result = self.datastore.query(
                _query_embedding,
                self.top_k,
            )
            return result
        except Exception as e:
            raise Exception(f"{e}")
