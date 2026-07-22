from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load pretrained AI model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(image, return_tensors="pt")

    output = model.generate(
    **inputs,
    max_length=50,
    num_beams=5,
    repetition_penalty=2.0
)

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption