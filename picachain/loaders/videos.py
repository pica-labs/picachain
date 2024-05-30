import os
from datetime import timedelta
from typing import List

import cv2
from PIL import Image
from tqdm import tqdm

from picachain.loaders.base import Loader
from picachain.structures import Document
from picachain.utils.image_util import image_to_base64


class VideoLoader(Loader):
    """Load videos"""

    def __init__(self, path) -> None:
        super().__init__()
        self.path = path

    def _extract_frames(self, source: str):
        result = []
        video = cv2.VideoCapture(source)
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_number = 0
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        duration = str(timedelta(seconds=(frame_count / fps)))

        while True:
            ret, frame = video.read()
            if frame is not None:
                img = Image.fromarray(frame, "RGB")
                current_second = frame_number / fps
                timestamp = str(timedelta(seconds=current_second))
                content = image_to_base64(img)
                metadata = {
                    "frame": f"{frame_number}_{str(source)}",
                    "timestamp": timestamp,
                    "mode": img.mode,
                    "source": source,
                    "fps": fps,
                    "width": frame_width,
                    "height": frame_height,
                    "duration": duration,
                }

                result.append(Document(content=content, metadata=metadata))
            if not ret:
                break

            frame_number += 1

        video.release()
        return result

    def load(self):
        """load and parse video files into frames"""
        videos = []
        for root, dirs, files in os.walk(self.path):
            for file in tqdm(files, desc="Loading videos"):
                if file.split(".")[-1] in ["mp4", "mkv"]:
                    source = os.path.join(root, file)
                    videos.extend(self._extract_frames(source))
        return videos
