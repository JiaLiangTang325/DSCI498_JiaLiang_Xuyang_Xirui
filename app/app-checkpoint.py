import gradio as gr
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image


device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
).to(device)

pipe.safety_checker = None


def stylize(image, style, strength):
    if image is None:
        return None

    image = image.resize((512, 512))

    prompt = f"{style} painting style"

    result = pipe(
        prompt=prompt,
        image=image,
        strength=strength,
        guidance_scale=7.5
    ).images[0]

    return result



demo = gr.Interface(
    fn=stylize,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Dropdown(
            ["Van Gogh", "Monet", "Cubism"],
            label="Choose Style"
        ),
        gr.Slider(0.2, 0.9, value=0.6, label="Stylization Strength")
    ],
    outputs=gr.Image(label="Stylized Image"),
    title="🎨 Diffusion-Based Image Stylization",
    description="Upload an image and apply artistic styles using Stable Diffusion."
)


demo.launch()