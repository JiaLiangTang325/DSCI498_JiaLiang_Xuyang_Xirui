# DSCI498_JiaLiang_Xuyang_Xirui
# Diffusion-Based Image Stylization

A research-oriented project exploring **image stylization using diffusion models** and comparing them with **traditional CNN-based neural style transfer** methods.

This project investigates the effectiveness of **Stable Diffusion for artistic style transfer**, analyzes the influence of **stylization strength**, and evaluates results using **quantitative metrics such as SSIM and CLIP Score**. A complete **web-based system** is also developed for interactive stylization.

---

# Example Results

| Original | Van Gogh | Monet | Cubism |
|----------|----------|--------|--------|
| ![](results/original.png) | ![](results/content_01_vangogh.png) | ![](results/content_01_monet.png) | ![](results/content_01_cubism.png) |

---

# Project Overview

Image style transfer transforms a content image into an artistic style while preserving structure.

Traditional methods rely on **CNN-based neural style transfer**, but they suffer from limited diversity and slow optimization.

This project explores:

- Diffusion-based image stylization using **Stable Diffusion**
- Comparison with **CNN-based neural style transfer**
- Analysis of stylization strength
- Structural guidance for improved consistency
- Development of a **web-based stylization system**

---

# Web Application (Final System)

We implemented a **Gradio-based web interface** for real-time stylization.

### Features

- Upload an image
- Select artistic style (Van Gogh / Monet / Cubism)
- Adjust stylization strength
- Enable structural guidance
- Generate stylized output

### Run the App

```bash
python app/app.py
```

Then open the public link generated in the terminal:

```
https://xxxxx.gradio.live
```

> Note: The link is temporary and active only while the app is running.

---

# Project Structure

```
diffusion-style-transfer-project
│
├── app
│   └── app.py                  # Web interface
│
├── models
│   └── diffusion_pipeline.py  # Core stylization logic
│
├── data
│   ├── content
│   └── style
│
├── notebooks                  # Experiments
├── results                    # Generated images
├── README.md
└── requirements.txt
```

---

# Methodology

## Diffusion-Based Stylization

We use **Stable Diffusion (img2img)**:

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

- CNN → better structure
- Diffusion → richer artistic styles

---

## Stylization Strength

We study the `strength` parameter:

| Strength | Effect |
|---------|--------|
| 0.3 | High structure preservation |
| 0.6 | Balanced |
| 0.9 | Strong stylization |

---

## Structural Guidance

We introduce a simple method:

- Edge enhancement preprocessing
- Improves structure preservation

---

## Quantitative Evaluation

### SSIM

Measures structure similarity.

### CLIP Score

Measures style alignment.

---

# Experimental Results

```
Average SSIM ≈ 0.32
CLIP Score ≈ 0.28
```

Findings:

- Diffusion produces diverse artistic styles
- Structure is partially preserved
- Strength controls trade-off

---

# Known Issues

Some outputs may appear black due to:

- Diffusion randomness
- High stylization strength
- GPU memory limits

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

- ControlNet for advanced structural guidance
- User study evaluation
- Online deployment

---

# References

1. Gatys et al., Neural Style Transfer  
2. Rombach et al., Stable Diffusion  
3. Radford et al., CLIP
