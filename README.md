# DSCI498_JiaLiang_Xuyang_Xirui
# Diffusion-Based Image Stylization

A research-oriented project exploring **image stylization using diffusion models** and comparing them with **traditional CNN-based neural style transfer** methods.

This project investigates the effectiveness of **Stable Diffusion for artistic style transfer**, analyzes the influence of **stylization strength**, and evaluates results using **quantitative metrics such as SSIM and CLIP Score**. A complete **web-based system** is also developed for interactive stylization.

---

# Project Overview

Image style transfer aims to transform a content image into the artistic style of a target domain (e.g., Van Gogh, Monet, Cubism).

Traditional approaches rely on **CNN-based neural style transfer**, which optimize feature representations in deep convolutional networks. While effective, these methods often produce limited diversity and require computationally expensive optimization.

Recent **diffusion models** provide a new paradigm for high-quality image generation and stylization.

This project explores:

- Diffusion-based image stylization using Stable Diffusion
- Comparison with CNN-based neural style transfer
- Analysis of stylization strength
- Structural guidance for improved consistency
- Development of a web-based stylization system

---

# Web Application (Final System)

We developed an interactive web application using **Gradio**.

## Features

- Upload an image
- Select artistic style (Van Gogh / Monet / Cubism)
- Adjust stylization strength
- Enable structural guidance
- Generate stylized output

## Run the App

```bash
python app/app.py
```

Then open the public link generated in the terminal:

```
https://xxxxx.gradio.live
```

> Note: The link is temporary and only active while the application is running.

---

# Project Structure

```
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
├── README.md
└── requirements.txt
```

---

# Methodology

## Diffusion-Based Stylization

We use Stable Diffusion (img2img) to generate stylized images:

```
content image → diffusion model → stylized image
```

Example prompts:

```
Van Gogh painting style
Monet impressionist painting
Cubism painting style
```

---

## CNN-Based Baseline

We compare with traditional neural style transfer:

- CNN → better structure preservation  
- Diffusion → richer artistic styles  

---

## Stylization Strength

We study the effect of the `strength` parameter:

| Strength | Effect |
|---------|--------|
| 0.3 | High structure preservation |
| 0.6 | Balanced |
| 0.9 | Strong stylization |

---

## Structural Guidance

We introduce a simple structural guidance method:

- Edge enhancement preprocessing
- Improves structure preservation

---

## Quantitative Evaluation

### SSIM

Measures structural similarity between original and stylized images.

### CLIP Score

Measures alignment between generated image and target style.

---

# Experimental Results

```
Average SSIM ≈ 0.32
CLIP Score ≈ 0.28
```

Key observations:

- Diffusion produces visually rich styles
- Structure is partially preserved
- Stylization strength controls trade-off

---

# Known Issues

Some generated images may appear black due to:

- Diffusion randomness
- High stylization strength
- GPU memory limitations

---

# Environment Setup

```bash
pip install -r requirements.txt
```

---

# Hardware

- GPU: ~8GB VRAM
- Framework: PyTorch
- Library: Hugging Face Diffusers

---

# Future Work

- Advanced structural guidance (e.g., ControlNet)
- User study for perceptual evaluation
- Online deployment

---

# References

1. Gatys et al., Neural Style Transfer  
2. Rombach et al., Stable Diffusion  
3. Radford et al., CLIP
