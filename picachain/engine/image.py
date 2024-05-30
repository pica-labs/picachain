from typing import List

from tqdm import tqdm

from picachain.structures import Document
from picachain.utils.image_util import image_to_base64


class ImageEngine:
    @staticmethod
    def process_image_documents(images: List[Document]):
        # convert the img to base64
        images = [
            Document(content=image_to_base64(doc.content), metadata=doc.metadata)
            for doc in tqdm(images)
        ]
        return images
