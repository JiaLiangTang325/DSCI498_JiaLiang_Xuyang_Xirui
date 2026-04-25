Project Title:
Diffusion-Based Image Stylization

Team Members:
JiaLiang Tang
Xuyang Wang
Xirui Li

Project Description:
This project explores image stylization using Stable Diffusion and compares diffusion-based stylization with traditional CNN-based neural style transfer. The project includes diffusion stylization, CNN baseline comparison, strength parameter analysis, quantitative evaluation using SSIM and CLIP Score, and an interactive Gradio web application.

How to Run:
1. Install dependencies:
   pip install -r requirements.txt

2. Run the web application:
   python main.py

3. The app will launch a Gradio interface. If share=True is enabled in app/app.py, a public Gradio link will be generated.

Main Files:
- main.py: main entry point for running the web application
- app/app.py: Gradio web interface
- models/diffusion_pipeline.py: Stable Diffusion stylization pipeline
- notebooks/: experimental notebooks
- results/: generated stylization results
- data/: content and style images or data description

Notes:
The Gradio public link is temporary and only active while the application is running.