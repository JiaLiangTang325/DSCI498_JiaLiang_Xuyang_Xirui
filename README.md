# DSCI498_JiaLiang_Xuyang_Xirui
# Diffusion-Based Image Stylization

A research-oriented project exploring **image stylization using diffusion models** and comparing them with **traditional CNN-based neural style transfer** methods.

This project investigates the effectiveness of **Stable Diffusion for artistic style transfer**, analyzes the influence of **stylization strength**, and evaluates results using **quantitative metrics such as SSIM and CLIP Score**.

---

# Project Overview

Image style transfer aims to transform a content image into the artistic style of a target domain (e.g., Van Gogh, Monet, Cubism).

Traditional approaches rely on **CNN-based neural style transfer**, which optimizes feature representations in deep convolutional networks. While effective, these methods often produce limited diversity and may require expensive optimization.

Recent **diffusion models** have demonstrated strong generative capabilities and provide a new paradigm for image stylization.

This project explores:

- Diffusion-based image stylization using **Stable Diffusion**
- Comparison with **CNN-based neural style transfer**
- The impact of **stylization strength on content preservation**
- Quantitative evaluation using **SSIM and CLIP Score**

---

# Project Structure

```
diffusion-style-transfer-project
│
├── data
│   ├── content
│   │   └── input images
│   │
│   └── style
│       ├── vangogh
│       ├── monet
│       └── cubism
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
│   └── generated images
│
├── README.md
└── requirements.txt
```

---

# Methodology

The project consists of several experimental stages.

---

## 1. Diffusion-Based Stylization

Implemented using **Stable Diffusion img2img pipeline** from the Hugging Face `diffusers` library.

Process:

```
content image
      ↓
diffusion img2img
      ↓
style prompt
      ↓
stylized image
```

Example prompts:

```
Van Gogh painting style
Monet impressionist painting
Cubism painting style
```

---

## 2. Batch Stylization

A batch pipeline is implemented to generate stylized images for multiple content inputs and style prompts.

Input:

- Content images from `data/content`

Output:

- Stylized images stored in `results/`

Naming convention:

```
contentID_style.png
```

Example:

```
content_01_vangogh.png
content_02_monet.png
content_03_cubism.png
```

---

## 3. CNN-Based Neural Style Transfer

To provide a baseline comparison, traditional **Neural Style Transfer** based on CNN feature optimization is implemented.

Reference:

Gatys et al., *Image Style Transfer Using Convolutional Neural Networks*

Pipeline:

```
content image
+
style image
↓
CNN feature optimization
↓
stylized output
```

---

## 4. Stylization Strength Experiment

Diffusion img2img introduces a parameter:

```
strength
```

which controls how strongly the output deviates from the original image.

Experiments were conducted using:

```
strength = 0.3
strength = 0.6
strength = 0.9
```

Key observation:

- Lower strength preserves content structure.
- Higher strength increases stylization but may distort image structure.

---

## 5. Quantitative Evaluation

Two metrics are used to evaluate stylization results.

### Structural Similarity (SSIM)

Measures structural similarity between the original and stylized images.

Range:

```
0 - 1
```

Higher values indicate better structural preservation.

---

### CLIP Score

Uses a **CLIP model** to evaluate the semantic similarity between generated images and textual prompts.

Higher values indicate stronger alignment with the target style description.

---

# Experimental Results

Example results from the evaluation stage:

```
Average SSIM ≈ 0.32
CLIP Score ≈ 0.28
```

Interpretation:

- Diffusion stylization produces visually rich styles.
- Content structure is partially preserved.
- Stylization strength significantly affects results.

---

# Known Issues

During batch generation, a small number of generated images appeared completely black.

Possible reasons include:

- The stochastic nature of diffusion models
- High stylization strength parameters
- GPU memory limitations during batch inference

Invalid outputs were excluded from the quantitative evaluation.

---

# Environment Setup

Install dependencies:

```
pip install -r requirements.txt
```

Example requirements:

```
torch
diffusers
transformers
open_clip_torch
scikit-image
matplotlib
```

---

# Hardware

Experiments were conducted on:

```
GPU: NVIDIA GPU (≈8GB VRAM)
Framework: PyTorch
Library: Hugging Face Diffusers
```

---

# Future Work

Planned extensions include:

- Structural guidance using **ControlNet**
- Human **user study** for perceptual evaluation
- Development of a **web-based stylization interface**

---

# References

1. Gatys et al., *Image Style Transfer Using Convolutional Neural Networks*
2. Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*
3. Radford et al., *Learning Transferable Visual Models From Natural Language Supervision*
