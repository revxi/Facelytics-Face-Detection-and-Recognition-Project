# 🌟 Facelytics – Face Detection and Recognition Project

Facelytics is a cutting-edge AI project that performs real-time **face detection** and **face recognition** using deep learning techniques. It offers an intuitive and interactive interface built with **Streamlit**, allowing users to upload photos, identify known individuals, and even recognized.

📸 Features

✅ Real-time face detection  
✅ Face recognition using known face embeddings  
✅ Add new faces dynamically to the system  
✅ Live webcam face recognition (via OpenCV)  
✅ Emotion detection (Happy, Sad, Neutral, etc.)  
✅ Attendance logging with timestamps  
✅ Search and verify identity with confidence score  
✅ Simple and intuitive Streamlit interface  
✅ Fully offline functionality after setup

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI Framework)
- **face_recognition** (dlib based)
- **OpenCV** (Camera & Image processing)
- **NumPy**
- **Pillow**
- **Emotion detection** using deep learning (FER or CNN models)

---

## 🚀 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/revxi/Facelytics-Face-Detection-and-Recognition-Project.git
   cd Facelytics-Face-Detection-and-Recognition-Project

2. Install Dependencies

pip install -r requirements.txt


3. Run the App

streamlit run app.py


4. Upload Images or Use Webcam

Upload an image in the app to test face recognition

Click “Capture from Webcam” (if enabled)





---

🗂️ Project Structure

Facelytics/
│
├── app.py                    # Streamlit app
├── requirements.txt          # Project dependencies
├── known_faces/              # Folder to store known face encodings
├── uploaded_images/          # Temporary folder for uploaded files
├── assets/                   # (Optional) For adding UI images or icons
└── .gitignore


---

🧠 Future Enhancements

✅ Emotion recognition

✅ Attendance CSV export

🔄 Face clustering for unknown persons

🔄 Mobile responsiveness for Streamlit UI

🔄 Face blur for anonymization

🔄 Admin dashboard with user stats



---

📷 Screenshots (optional)

Add screenshots here to show how it works visually


---

🤝 Contribution

Feel free to fork the repo, open issues, or submit PRs. All contributions and suggestions are welcome!


---

📜 License

MIT License © 2025 @revxi


---

🌈 Live Like You Mean It

> “Facelytics helps machines know the face behind the screen — responsibly and smartly.”
