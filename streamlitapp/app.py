import streamlit as st
from projectmlincvmediapipe import demo
from PIL import Image
import numpy as np

st.title("Welcome to my demo web app")
st.write("The model applied in this project is Mediapipe Meet Segmentation, which segment a human out of background from a selfie picture.")

file_upload = st.file_uploader("Upload image here", type=["jpg","jpeg", "png"])

if file_upload is not None:
    img = Image.open(file_upload)
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, "Original image")

    img_numpy = np.array(img.convert('RGB'))
    output, out1, out2, out3 = demo.main(img_numpy)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(out1, "output 1")
    with col2:
        st.image(out2, "output 2")
    with col3:
        st.image(out3, "output 3")