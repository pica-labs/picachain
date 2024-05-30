from typing import List, Union

import numpy as np
from PIL import Image

from picachain.embedding.base import Embedding
from picachain.structures import Document


class ClipEmbedding(Embedding):
    def __init__(self):
        """Initiate the clip embedding"""
        try:
            import torch
            from transformers import CLIPModel, CLIPProcessor, CLIPTokenizer
        except ImportError as e:
            raise ImportError(
                "Could not import torch, transformers. Please install it with `pip install torch transformers`"
            ) from e

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(
            self.device
        )
        self.tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32")

    def save(self, path: str):
        self.model.save_pretrained(path)
        self.processor.save_pretrained(path)

    def encode_image(self, image: Document):
        raise NotImplementedError

    def encode_text(self, text: str):
        raise NotImplementedError

    def encode_images(self, images: List[Union[Document, Image.Image]]) -> np.ndarray:
        """
        Encode a list of images using the clip model.

        Args:
        - images (list): A list of images to be encoded.

        Returns:
        - numpy.ndarray: An array of image embeddings of shape (len(images), 512).
        """

        if isinstance(images[0], Document):
            images = [doc.content for doc in images]

        image = self.processor(text=None, images=images, return_tensors="pt")[
            "pixel_values"
        ].to(self.device)
        embedding = self.model.get_image_features(image)
        # convert the embeddings to numpy array
        return embedding.cpu().detach().numpy()
