# DSCI498_JiaLiang_Xuyang_Xirui

# Diffusion-Based Image Stylization

A research-oriented project exploring **image stylization using diffusion models** and comparing them with **traditional CNN-based neural style transfer** methods.

This project investigates the effectiveness of **Stable Diffusion for artistic style transfer**, analyzes the influence of **stylization strength**, evaluates results using **quantitative metrics such as SSIM and CLIP Score**, and provides an interactive web-based interface for demonstrating the stylization workflow.

---

## Project Overview

Image style transfer aims to transform a content image into the artistic style of a target domain, such as Van Gogh, Monet, or Cubism, while preserving the original structure of the input image.

Traditional approaches rely on **CNN-based neural style transfer**, which optimizes feature representations extracted from deep convolutional networks. While CNN-based methods can preserve content structure relatively well, they often produce limited style diversity and require expensive per-image optimization.

Recent **diffusion models**, such as Stable Diffusion, provide a more flexible and expressive approach for image generation and stylization. In this project, we explore diffusion-based stylization and compare it with a CNN-based baseline.

This project includes:

- Diffusion-based image stylization using Stable Diffusion
- CNN-based neural style transfer baseline comparison
- Stylization strength analysis
- Simple structural guidance using edge enhancement
- Quantitative evaluation using SSIM and CLIP Score
- A Streamlit-based deployed interface
- A Gradio/local GPU demo for full image generation

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
- View the overall interaction workflow

### Streamlit Web App Link

```text
[Insert your Streamlit app link here]
