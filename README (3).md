# 🤖 Facelytics

**Smart Face Detection & Recognition Web App with Streamlit**

Facelytics is a Python-based AI web application that detects and recognizes faces in uploaded images using powerful computer vision and deep learning techniques. With a clean Streamlit UI, users can easily upload images and view recognized faces with bounding boxes and name tags. This project is ideal for applications like smart attendance systems, photo tagging, access control, and face-based user identification.

---

## 🌟 Features

- 📸 Upload any image through a simple web interface  
- 🔍 Automatically detects all faces in the image  
- 🧠 Recognizes pre-registered faces and displays names  
- 🖼️ Visual output with bounding boxes and labels  
- 💡 Extendable with real-time webcam support and advanced models

---

## 🛠️ Tech Stack

| Component       | Technology                          |
|----------------|--------------------------------------|
| Language        | Python 3.x                          |
| Face Detection  | `face_recognition`, `OpenCV`, `dlib`|
| Web Framework   | `Streamlit`                         |
| Image Handling  | `NumPy`, `PIL`                      |
| Optional Models | `MTCNN`, `ArcFace`, `Siamese Net`   |

---

## 📁 Folder Structure

facelytics/ ├── known_faces/          # Images of registered users ├── sample/               # Sample test images ├── app.py                # Main Streamlit application ├── requirements.txt      # Required Python packages └── README.md             # You're reading this!

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/facelytics.git
cd facelytics

2. Install Dependencies

pip install -r requirements.txt

3. Add Known Faces

Place clear images of known individuals inside the known_faces/ directory. Filenames will be used as display names (e.g., diwi.jpg ➜ "diwi").

4. Start the Streamlit App

streamlit run app.py


---

🎯 Use Cases

✅ Smart attendance systems

✅ Employee verification

✅ Automated image tagging

✅ Access control systems

✅ Personalized customer interaction



---

🧠 Future Enhancements

Real-time webcam integration

Dynamic registration of new faces via UI

Advanced recognition with ArcFace or Siamese Networks

Secure face data storage

Deployment on Streamlit Cloud or Hugging Face Spaces



---

💙 About the Creator

Facelytics is built by Diksha (Reverie), a passionate final-year Computer Engineering student who loves AI, intuitive UI design, and creating smart tech that actually feels good to use.


---

📜 License

This project is licensed under the MIT License.


---



