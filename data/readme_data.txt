Data README
===========

This file explains how to obtain the data used in this project and where to place the files.

Project:
Diffusion-Based Image Stylization

Data Types:
This project uses two types of images:

1. Content Images
2. Style Reference Images

--------------------------------------------------
1. Content Images
--------------------------------------------------

Content images are normal photographs used as input images for stylization.

Recommended sources:
- Unsplash: https://unsplash.com/
- Pexels: https://www.pexels.com/

Suggested search keywords:
- landscape
- city street
- portrait
- architecture
- animal
- nature

Recommended amount:
Approximately 100 content images.

Where to place them:
Place all content images inside:

data/content/

Example:

data/content/content_001.jpg
data/content/content_002.jpg
data/content/content_003.jpg

Recommended naming format:
content_001.jpg
content_002.jpg
content_003.jpg
...

--------------------------------------------------
2. Style Reference Images
--------------------------------------------------

Style images are artwork reference images used to represent different artistic styles.

Recommended source:
- WikiArt: https://www.wikiart.org/

Selected style categories:
- Van Gogh
- Monet
- Cubism

Suggested search keywords on WikiArt:
- Vincent van Gogh
- Claude Monet
- Cubism
- Pablo Picasso
- Georges Braque

Recommended amount:
Approximately 10 to 15 images per style category.

Where to place them:

Van Gogh style images:
data/style/vangogh/

Example:
data/style/vangogh/vangogh_01.jpg
data/style/vangogh/vangogh_02.jpg

Monet style images:
data/style/monet/

Example:
data/style/monet/monet_01.jpg
data/style/monet/monet_02.jpg

Cubism style images:
data/style/cubism/

Example:
data/style/cubism/cubism_01.jpg
data/style/cubism/cubism_02.jpg

--------------------------------------------------
Expected Folder Structure
--------------------------------------------------

After collecting the images, the data folder should look like this:

data/
|
|-- content/
|   |-- content_001.jpg
|   |-- content_002.jpg
|   |-- content_003.jpg
|   |-- ...
|
|-- style/
|   |
|   |-- vangogh/
|   |   |-- vangogh_01.jpg
|   |   |-- vangogh_02.jpg
|   |   |-- ...
|   |
|   |-- monet/
|   |   |-- monet_01.jpg
|   |   |-- monet_02.jpg
|   |   |-- ...
|   |
|   |-- cubism/
|       |-- cubism_01.jpg
|       |-- cubism_02.jpg
|       |-- ...

--------------------------------------------------
Notes
--------------------------------------------------

This project does not train Stable Diffusion from scratch.

The images are used for:
- Testing the stylization pipeline
- Generating experimental results
- Comparing CNN-based style transfer and diffusion-based stylization
- Evaluating results using SSIM and CLIP Score

Since the project uses a pretrained Stable Diffusion model, a curated dataset of representative images is sufficient.

If the full dataset is too large to submit, a smaller sample set may be included in the data folder, while this file explains how to reconstruct the complete dataset.
