import base64
import io

from PIL import Image


def image_to_base64(image: Image) -> str:
    """
    Converts a PIL Image to base64 encoding.

    Args:
        image: A PIL Image object.

    Returns:
        A base64 encoded string of the image.
    """
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_str}"


def base64_to_image(base64_str: str) -> Image:
    """
    Converts a base64 encoded string to a PIL Image.

    Args:
        base64_string: A base64 encoded string of the image.

    Returns:
        A PIL Image object.
    """
    # Remove the "data:image/jpeg;base64," part if present
    if base64_str.startswith("data:image/jpeg;base64,"):
        base64_str = base64_str[len("data:image/jpeg;base64,") :]

    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    return image
