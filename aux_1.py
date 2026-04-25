"""
Auxiliary file for Diffusion-Based Image Stylization Project.

This project mainly uses:
- app/app.py for the Gradio web interface
- models/diffusion_pipeline.py for the Stable Diffusion stylization pipeline
- notebooks/ for experiments and evaluation

The main entry point is:
python main.py
"""

from models.diffusion_pipeline import stylize