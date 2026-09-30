from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from .ai.config import BASE_DIR, ENV_FILE, HF_API_KEY, IMAGE_MODEL


load_dotenv(ENV_FILE)

IMAGE_DIR = BASE_DIR / "app" / "static" / "generated_images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)


def generate_image(prompt, panel_number):

    if not HF_API_KEY:
        raise RuntimeError(
            "HF_API_KEY not found. Please add your Hugging Face token to .env"
        )

    print(f"Generating AI image for panel {panel_number}...")

    client = InferenceClient(
        provider="auto",
        api_key=HF_API_KEY
    )

    image = client.text_to_image(
        prompt=prompt,
        model=IMAGE_MODEL
    )

    filename = f"panel_{panel_number}.png"

    image_path = IMAGE_DIR / filename

    image.save(str(image_path))

    print(f"AI IMAGE CREATED: {image_path}")

    return {
        "panel_number": panel_number,
        "image_url": f"/static/generated_images/{filename}",
        "image_path": str(image_path)
    }