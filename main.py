import os
import subprocess
import sys

if __name__ == "__main__":
    print("Starting Diffusion-Based Image Stylization Web App...")
    print("Please wait while the Stable Diffusion model is loading.")
    subprocess.run([sys.executable, "app/app.py"])