from pathlib import Path
from typing import List, Union

from PIL import Image
from tqdm import tqdm

from picachain.loaders.base import Loader
from picachain.loaders.image import ImageLoader
from picachain.models import Deplot
from picachain.structures import Document


class ChartParser:
    @classmethod
    def from_image(cls, image: Union[Path, Image.Image]) -> Document:
        if isinstance(image, Path):
            image = Image.open(image)
        result = Deplot.generate(image)
        return result


class ChartLoader(Loader):
    def __init__(self, path: Path) -> None:
        super().__init__()
        self.path = path

    def load(self) -> List[Document]:
        loader = ImageLoader(self.path)
        charts = []
        for img in tqdm(loader.load(), desc="Extracting info"):
            metadata = {
                "source": img,
                "size": img.size,
                "mode": img.mode,
            }
            charts.append(
                Document(
                    content=ChartParser.from_image(img),
                    metadata=metadata,
                )
            )
        return charts
