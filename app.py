import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌿"
)

st.title("🌿 PlantCare AI")
st.subheader("AI-Powered Plant Disease Detection")

st.write(
    "Upload a plant leaf photo to begin "
    "your disease screening."
)

photo = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if photo:
    image = Image.open(photo).convert("RGB")
    st.image(image, caption="Your plant leaf",
             use_container_width=True)

    st.info(
        "Image uploaded successfully! "
        "AI prediction will be added next."
    )
