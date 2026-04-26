import streamlit as st
from PIL import Image
from models.diffusion_pipeline import stylize

st.set_page_config(
    page_title="Diffusion-Based Image Stylization",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Diffusion-Based Image Stylization")

st.write(
    "Upload an image, choose an artistic style, adjust the stylization strength, "
    "and optionally enable structural guidance."
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
    st.info("Please upload an image to start stylization.")
else:
    input_image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(input_image, use_container_width=True)

    with col2:
        st.subheader("Stylized Image")

        if st.button("Generate Stylized Image"):
            with st.spinner("Generating image... This may take some time."):
                output_image = stylize(
                    input_image,
                    style,
                    strength,
                    use_structure_guidance
                )

            st.image(output_image, use_container_width=True)

            output_path = "stylized_output.png"
            output_image.save(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    label="Download Result",
                    data=file,
                    file_name="stylized_output.png",
                    mime="image/png"
                )