# DSCI498_JiaLiang_Xuyang_Xirui

# Diffusion-Based Image Stylization

A research-oriented course project exploring **image stylization using diffusion models** and comparing diffusion-based stylization with **traditional CNN-based neural style transfer** methods.

This project investigates the effectiveness of **Stable Diffusion** for artistic style transfer, analyzes the influence of the **stylization strength** parameter, evaluates generated results using **SSIM** and **CLIP Score**, and provides a web-based interface for demonstrating the stylization workflow.

---

## Project Overview

Image style transfer aims to transform a content image into the artistic style of a target domain while preserving the original structure of the input image. Example artistic styles include **Van Gogh**, **Monet**, and **Cubism**.

Traditional style transfer methods often rely on **CNN-based neural style transfer**, where feature representations from convolutional neural networks are used to optimize a generated image. These methods can preserve the structure of the original image relatively well, but they may produce limited style diversity and often require expensive per-image optimization.

Recent **diffusion models**, such as Stable Diffusion, provide a more flexible and expressive approach for image generation and stylization. In this project, we explore diffusion-based image stylization and compare it with a CNN-based baseline.

This project includes:

- Diffusion-based image stylization using Stable Diffusion
- CNN-based neural style transfer baseline comparison
- Stylization strength analysis
- Simple structural guidance using edge enhancement
- Quantitative evaluation using SSIM and CLIP Score
- A Streamlit-based deployed interface
- A Gradio/local GPU demo for full Stable Diffusion image generation

---

## Web Application

This project provides two web interfaces for demonstration purposes.

### 1. Streamlit Web Interface

The Streamlit version is deployed as a public web interface to demonstrate the main workflow of the system.

Users can:

- Upload an image
- Select an artistic style: Van Gogh, Monet, or Cubism
- Adjust the stylization strength
- Enable structural guidance
- View the overall user workflow

### Streamlit Web App Link

https://dsci498jialiangxuyangxirui-hzh8czogghfdmlfs2sarrf.streamlit.app/

### Deployment Note

Stable Diffusion inference is GPU-intensive. Due to limited GPU availability in the deployed Streamlit cloud environment, the public Streamlit version mainly demonstrates the **user interface and workflow**.

The fully working image generation version is demonstrated in the final presentation video using a local GPU environment.

This is a deployment hardware limitation rather than an implementation issue.

---

### 2. Gradio / Local GPU Demo

The full image generation pipeline is demonstrated using a local Gradio app with GPU acceleration.

To run the local Gradio version:

```bash
python app/app.py

The app provides:

Image upload
Style selection
Stylization strength control
Structural guidance option
Actual Stable Diffusion image generation

During the final video presentation, the local GPU version is used to demonstrate the complete stylization process and generated results.

Project Structure
diffusion-style-transfer-project
│
├── app
│   └── app.py
│
├── models
│   └── diffusion_pipeline.py
│
├── data
│   ├── content
│   └── style
│
├── notebooks
│   ├── 01_diffusion_test.ipynb
│   ├── 02_style_transfer.ipynb
│   ├── 03_batch_style_transfer.ipynb
│   ├── 04_cnn_style_transfer.ipynb
│   ├── 05_strength_experiment.ipynb
│   └── 06_quantitative_evaluation.ipynb
│
├── results
├── streamlit_app.py
├── requirements.txt
├── README.md
└── ReadMe.txt
Dataset

The dataset used in this project consists of two types of images: content images and style reference images.

Content Images

Content images are natural photographs used as input images for stylization.

Approximately 100 content images were collected from public image sources such as Unsplash and Pexels. These images include landscapes, portraits, architecture, and everyday scenes.

Style Images

Style reference images were collected for three artistic categories:

Van Gogh
Monet
Cubism

Each style category contains approximately 10–15 reference images.

Since this project uses pretrained Stable Diffusion and does not train a model from scratch, the dataset is mainly used for testing, evaluation, and demonstration.

Methodology
1. Diffusion-Based Stylization

We use Stable Diffusion in an image-to-image setting.

The basic workflow is:

content image → Stable Diffusion img2img → stylized image

Example prompts include:

Van Gogh painting style
Monet impressionist painting
Cubism painting style

The model receives a content image and a style prompt, then generates a stylized output image.

2. CNN-Based Baseline

To provide a comparison, we also implemented a traditional CNN-based neural style transfer method.

The CNN baseline is used to compare traditional neural style transfer with diffusion-based stylization.

General observations:

CNN-based style transfer preserves structure better
Diffusion-based stylization produces richer and more diverse artistic styles
Diffusion models provide more flexible parameter control
3. Stylization Strength Analysis

We studied the effect of the strength parameter in the Stable Diffusion image-to-image pipeline.

The strength parameter controls how strongly the generated image deviates from the original input image.

Strength	Effect
0.3	High structure preservation, weaker style effect
0.6	Balanced structure and style
0.9	Strong stylization, possible structure distortion

This experiment demonstrates the trade-off between content preservation and artistic stylization.

4. Structural Guidance

We introduced a simple structural guidance method using edge enhancement preprocessing.

The purpose is to strengthen object boundaries before stylization and improve structure preservation.

This lightweight method serves as a practical alternative to more advanced structural control approaches such as ControlNet.

5. Quantitative Evaluation

We used two metrics to evaluate the generated results.

SSIM

SSIM measures structural similarity between the original content image and the stylized output.

A higher SSIM value indicates better structure preservation.

CLIP Score

CLIP Score measures semantic alignment between the generated image and the target style prompt.

A higher CLIP Score indicates stronger alignment with the intended artistic style.

Experimental Results

Example quantitative results:

Average SSIM ≈ 0.32
CLIP Score ≈ 0.28

Key observations:

Diffusion produces visually rich artistic styles
Content structure is partially preserved
Stylization strength strongly affects the structure-style trade-off
Structural guidance helps improve edge and boundary preservation
Diffusion results are generally more diverse than CNN-based results
Known Issues

During batch stylization, some generated images appeared completely black.

Possible causes include:

Diffusion model randomness
High stylization strength
GPU memory limitations during batch inference

These invalid outputs were excluded from quantitative evaluation.

Environment Setup

Install dependencies:

pip install -r requirements.txt

Example dependencies:

streamlit
torch
torchvision
diffusers
transformers
accelerate
safetensors
pillow
numpy
How to Run
Run the Streamlit Interface
streamlit run streamlit_app.py
Run the Local Gradio GPU Demo
python app/app.py

The local Gradio version is recommended for full Stable Diffusion inference because it can use local GPU acceleration.

Hardware

The full image generation system was tested locally using:

GPU: NVIDIA GPU with approximately 8GB VRAM
Framework: PyTorch
Library: Hugging Face Diffusers

The deployed Streamlit version may not perform full Stable Diffusion inference efficiently due to limited cloud hardware resources.

Final Deliverables

This project includes the following deliverables:

Final presentation video
Project poster
Source code files
Streamlit web app link
Local Gradio demo for full GPU-based image generation
Experimental notebooks
Generated result images
README and setup instructions
Future Work

Possible future improvements include:

Advanced structural guidance using ControlNet
More extensive user study evaluation
Online deployment with GPU-backed inference
Support for additional artistic styles
Faster inference optimization
References
Gatys et al., Neural Style Transfer
Rombach et al., Stable Diffusion
Radford et al., CLIP
