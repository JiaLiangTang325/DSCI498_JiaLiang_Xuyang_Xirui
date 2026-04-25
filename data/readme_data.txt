Data Description:

This project uses two types of images:

1. Content Images:
Content images are natural photographs used as input images for stylization.
They were collected from public image sources such as Unsplash and Pexels.
The images include landscapes, portraits, architecture, and everyday scenes.

2. Style Images:
Style images are artistic reference images representing different styles.
The selected styles include:
- Van Gogh
- Monet
- Cubism

Each style category contains approximately 10–15 reference images.

Dataset Purpose:
The dataset is used for testing and evaluating stylization results.
Since this project uses pretrained Stable Diffusion and does not train a model from scratch, a curated dataset of representative images is sufficient for experiments.

Folder Structure:
data/
├── content/
└── style/
    ├── vangogh/
    ├── monet/
    └── cubism/