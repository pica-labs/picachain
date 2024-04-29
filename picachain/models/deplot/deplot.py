from PIL import Image


class Deplot:
    model_id = "google/deplot"

    try:
        from transformers import (
            Pix2StructForConditionalGeneration,
            Pix2StructProcessor,
        )
    except ImportError:
        raise ImportError(
            "Failed to import transformers. Install using `pip install transformers`"
        )

    processor = Pix2StructProcessor.from_pretrained(model_id)
    model = Pix2StructForConditionalGeneration.from_pretrained(model_id)

    @classmethod
    def generate(cls, image: Image.Image) -> str:
        inputs = cls.processor(
            images=image,
            text="Generate underlying data table of the figure below:",
            return_tensors="pt",
        )
        predictions = cls.model.generate(**inputs, max_new_tokens=512)
        result = cls.processor.decode(predictions[0], skip_special_tokens=True)
        if result is not None:
            return str(result)
        else:
            return ""
