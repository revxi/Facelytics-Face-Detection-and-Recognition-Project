import streamlit as st
import face_recognition
import numpy as np
import cv2
from PIL import Image
import os

# Title
st.set_page_config(page_title="Facelytics", layout="centered")
st.title("📸 Facelytics – Face Detection & Recognition")

# Load known faces from the 'known_faces/' folder
def load_known_faces(folder="known_faces"):
    known_encodings = []
    known_names = []

    for filename in os.listdir(folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            path = os.path.join(folder, filename)
            image = face_recognition.load_image_file(path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_encodings.append(encoding[0])
                known_names.append(os.path.splitext(filename)[0])
    return known_encodings, known_names

known_encodings, known_names = load_known_faces()

# Sidebar options
option = st.sidebar.radio("Choose input method:", ("Upload Image", "Use Webcam (Local Only)"))

# Face recognition function
def recognize_faces(img, known_encodings, known_names):
    rgb_img = img[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)
    pil_img = Image.fromarray(img)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if face_distances.size > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(img, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    return img

# Upload Image
if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image with faces", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result_image = recognize_faces(image, known_encodings, known_names)
        st.image(result_image, caption="Detected Faces", use_column_width=True)

# Webcam (Only works locally)
elif option == "Use Webcam (Local Only)":
    st.warning("⚠️ Webcam works only when running locally.")
    if st.button("Start Webcam"):
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            result_frame = recognize_faces(frame, known_encodings, known_names)
            stframe.image(result_frame[:, :, ::-1], channels="RGB", use_column_width=True)

        cap.release()

# Footer
st.markdown("---")
st.markdown("💡 Tip: Place known face images in the `known_faces/` directory.")