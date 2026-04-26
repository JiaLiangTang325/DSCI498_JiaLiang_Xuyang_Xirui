Project Title:
Diffusion-Based Image Stylization

Course:
DSCI/CSE-498 Final Project

Team Members:
JiaLiang Tang
Xuyang Wang
Xirui Li

Short Description:
This project explores image stylization using diffusion models and compares diffusion-based stylization with traditional CNN-based neural style transfer. The system uses Stable Diffusion for image-to-image stylization, supports multiple artistic styles, analyzes stylization strength, applies simple structural guidance, and evaluates results using SSIM and CLIP Score.

Main Features:
1. Diffusion-based image stylization using Stable Diffusion
2. CNN-based neural style transfer baseline comparison
3. Stylization strength analysis
4. Simple structural guidance using edge enhancement
5. Quantitative evaluation using SSIM and CLIP Score
6. Streamlit web interface for workflow demonstration
7. Local Gradio demo for full GPU-based image generation

Web App Link:
https://dsci498jialiangxuyangxirui-hzh8czogghfdmlfs2sarrf.streamlit.app/

Important Deployment Note:
Stable Diffusion inference is GPU-intensive. Due to limited GPU availability in the deployed Streamlit cloud environment, the public Streamlit version mainly demonstrates the user interface and workflow.

The fully working image generation version is demonstrated in the final presentation video using a local GPU environment.

This is a deployment hardware limitation rather than an implementation issue.

How to Run the Streamlit Interface:
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   streamlit run streamlit_app.py

How to Run the Local Gradio GPU Demo:
1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python app/app.py

Recommended Demo Method:
The Streamlit link is used as the stable public web app link.
The local Gradio version is used in the final video to demonstrate actual Stable Diffusion image generation with GPU acceleration.

Project Structure:
diffusion-style-transfer-project
|
|-- app/
|   |-- app.py
|
|-- models/
|   |-- diffusion_pipeline.py
|
|-- data/
|   |-- content/
|   |-- style/
|
|-- notebooks/
|   |-- 01_diffusion_test.ipynb
|   |-- 02_style_transfer.ipynb
|   |-- 03_batch_style_transfer.ipynb
|   |-- 04_cnn_style_transfer.ipynb
|   |-- 05_strength_experiment.ipynb
|   |-- 06_quantitative_evaluation.ipynb
|
|-- results/
|
|-- streamlit_app.py
|-- requirements.txt
|-- README.md
|-- ReadMe.txt

Dataset:
The project uses approximately 100 content images collected from public image sources such as Unsplash and Pexels. The style reference images are organized into three categories: Van Gogh, Monet, and Cubism. Each style category contains approximately 10 to 15 reference images.

Since the project uses pretrained Stable Diffusion and does not train a model from scratch, the dataset is mainly used for testing, evaluation, and demonstration.

Method Summary:
The project uses Stable Diffusion in an image-to-image setting. A content image and a style prompt are provided to the model, and the model generates a stylized output image.

Example style prompts:
- Van Gogh painting style
- Monet impressionist painting
- Cubism painting style

The project also includes a CNN-based neural style transfer baseline for comparison.

Evaluation:
The generated images are evaluated using:
1. SSIM: measures structural similarity between original and stylized images.
2. CLIP Score: measures semantic alignment between generated images and target style prompts.

Example Results:
Average SSIM: approximately 0.32
CLIP Score: approximately 0.28

Known Issues:
Some generated images may appear completely black during batch stylization. Possible causes include diffusion randomness, high stylization strength, and GPU memory limitations. These invalid outputs were excluded from quantitative evaluation.

Final Deliverables:
1. Final presentation video
2. Project poster
3. Source code files
4. Streamlit web app link
5. Local Gradio demo for full GPU-based image generation
6. Experimental notebooks
7. Generated result images
8. README and setup instructions

Hardware:
The full image generation system was tested locally using an NVIDIA GPU with approximately 8GB VRAM.

Future Work:
1. Add advanced structural guidance using ControlNet
2. Conduct a larger user study
3. Deploy the full model using GPU-backed cloud infrastructure
4. Add more artistic styles
5. Optimize inference speed
6. Add additional evaluation metrics such as LPIPS or FID

References:
1. Gatys et al., Neural Style Transfer
2. Rombach et al., Stable Diffusion
3. Radford et al., CLIP
