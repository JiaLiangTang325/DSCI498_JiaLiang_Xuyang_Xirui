import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Diffusion-Based Image Stylization",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Diffusion-Based Image Stylization")

st.write(
    "This is the web interface for our diffusion-based image stylization system. "
    "The full Stable Diffusion model runs locally with GPU acceleration in our final demo video."
)

st.sidebar.header("Settings")

style = st.sidebar.selectbox(
    "Choose Style",
    ["Van Gogh", "Monet", "Cubism"]
)

strength = st.sidebar.slider(
    "Stylization Strength",
    min_value=0.2,
    max_value=0.9,
    value=0.6,
    step=0.1
)

use_structure_guidance = st.sidebar.checkbox(
    "Enable Structural Guidance",
    value=False
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is None:
    st.info("Please upload an image to start.")
else:
    input_image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(input_image, use_container_width=True)

    with col2:
        st.subheader("Stylization Settings")
        st.write(f"**Selected Style:** {style}")
        st.write(f"**Strength:** {strength}")
        st.write(f"**Structural Guidance:** {use_structure_guidance}")

        st.warning(
            "Stable Diffusion inference is GPU-intensive. "
            "The deployed cloud version shows the interface, while the final video demonstrates the working local GPU version."
        )
