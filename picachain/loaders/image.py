import os
import time
import uuid
from pathlib import Path

from PIL import Image
from tqdm import tqdm

from picachain.loaders.base import Loader
from picachain.structures import Document


class ImageLoader(Loader):
    """Image loader for loading an image or load batch of images from directory"""

    def __init__(self, path: Path) -> None:
        """
        path: directory containing the images
        """
        super().__init__()
        self.path = path

    def _generate_id(self, image):
        """Generate id for image"""
        base_id = uuid.uuid5(uuid.NAMESPACE_URL, image.__str__())
        timestamp = int(time.time() * 1000)
        return f"{base_id}-{timestamp}"

    def load(self) -> list:
        if os.path.isfile(self.path):
            return [Image.open(self.path)]
        elif os.path.isdir(self.path):
            images = []
            for img in tqdm(os.listdir(self.path), desc="Loading content"):
                _image = Image.open(os.path.join(self.path, img))
                images.append(
                    Document(
                        content=_image,
                        metadata={
                            "source": str(self.path),
                            "id": self._generate_id(_image),
                        },
                    )
                )
            return images
