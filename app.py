import streamlit as st
import face_recognition
import cv2
import numpy as np
from PIL import Image
import os

st.set_page_config(page_title="Facelytics", layout="centered")
st.title("👁️ Facelytics: Face Detection and Recognition")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = face_recognition.load_image_file(uploaded_file)
    face_locations = face_recognition.face_locations(image)

    # Draw rectangles on image
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    for top, right, bottom, left in face_locations:
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)

    st.image(image_bgr, channels="BGR", caption=f"Detected {len(face_locations)} face(s)")
else:
    st.info("Please upload an image to begin face detection.")