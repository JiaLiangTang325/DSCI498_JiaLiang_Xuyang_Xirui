
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import ImageFilter

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

pipe.enable_attention_slicing()
pipe.safety_checker = None


def stylize(image, style, strength, use_structure_guidance=False):
    if image is None:
        return None

    image = image.convert("RGB")
    image = image.resize((512, 512))

    if use_structure_guidance:
        image = image.filter(ImageFilter.EDGE_ENHANCE)

    prompt = f"{style} painting style"

    result = pipe(
        prompt=prompt,
        image=image,
        strength=strength,
        guidance_scale=7.5,
        num_inference_steps=20
    ).images[0]

    return result
