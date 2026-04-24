import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
from models.diffusion_pipeline import stylize


def run_stylization(image, style, strength, use_structure_guidance):
    return stylize(image, style, strength, use_structure_guidance)


demo = gr.Interface(
    fn=run_stylization,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Dropdown(
            ["Van Gogh", "Monet", "Cubism"],
            label="Choose Style"
        ),
        gr.Slider(
            minimum=0.2,
            maximum=0.9,
            value=0.6,
            step=0.1,
            label="Stylization Strength"
        ),
        gr.Checkbox(
            label="Enable Structural Guidance",
            value=False
        )
    ],
    outputs=gr.Image(type="pil", label="Stylized Image"),
    title="🎨 Diffusion-Based Image Stylization",
    description=(
        "Upload an image, choose an artistic style, adjust the stylization strength, "
        "and optionally enable structural guidance."
    )
)

demo.launch(share=True)