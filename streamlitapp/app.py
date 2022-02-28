import numpy as np
import streamlit as st
from PIL import Image

from projectmlincvmediapipe import demo

st.title("Welcome to my demo web app")
st.write(
    "The model applied in this project is Mediapipe Meet Segmentation, which segment a human out of background from a selfie picture."
)

file_upload = st.file_uploader("Upload image here", type=["jpg", "jpeg", "png"])
score = 0.5

if file_upload is not None:
    img = Image.open(file_upload)
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, "Original image")

    img_numpy = np.array(img.convert("RGB"))
    h, w = img_numpy.shape[0], img_numpy.shape[1]

    output, out1, out2, out3 = demo.main(img_numpy)
    print("max out1: ", np.max(out1), "min out1:", np.min(out1))
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(out1, "output 1")
        green = np.copy(img_numpy)
        green[out1 > 180] = img_numpy[out1 > 180] * 0.7 + np.array([0, 255, 0]) * 0.3
        st.image(green, "original image with output 1 as mask")
    with col2:
        st.image(out2, "output 2")
        green = np.copy(img_numpy)
        green[out2 > 180] = img_numpy[out2 > 180] * 0.7 + np.array([0, 255, 0]) * 0.3
        st.image(green, "original image with output 2 as mask")
    with col3:
        st.image(out3, "output 3")
        green = np.copy(img_numpy)
        green[out3 > 180] = img_numpy[out3 > 180] * 0.7 + np.array([0, 255, 0]) * 0.3
        st.image(green, "original image with output 3 as mask")
