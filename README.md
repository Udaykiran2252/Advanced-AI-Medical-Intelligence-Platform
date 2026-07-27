# 🩺 Advanced AI Medical Intelligence Platform

## 📌 Project Overview

The **Advanced AI Medical Intelligence Platform** is an AI-powered web application developed to analyze Chest X-ray images and predict the presence of **Pneumonia** using a Convolutional Neural Network (CNN). The application also generates an AI-assisted medical report based on the prediction.

The project is built using **TensorFlow, FastAPI, and Streamlit**, providing an end-to-end workflow from image upload to prediction and report generation.

---

## 🚀 Features

- Upload Chest X-ray images
- Pneumonia detection using Deep Learning (CNN)
- Prediction confidence score
- AI-generated medical report
- FastAPI REST API
- Interactive Streamlit web interface
- Clean and user-friendly interface

---

## 🛠️ Technologies Used

### Programming Language
- Python 3.12

### Deep Learning
- TensorFlow
- Keras

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Image Processing
- OpenCV
- Pillow

### Libraries
- NumPy
- Requests

---

## 📂 Project Structure

```
Advanced-AI-Medical-Intelligence-Platform/
│
├── backend/
│   ├── app.py
│   ├── predict.py
│   ├── llm_report.py
│   └── __init__.py
│
├── frontend/
│   └── streamlit_app.py
│
├── models/
│   └── pneumonia_model.keras
│
├── uploads/
│
├── train_model.ipynb
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-AI-Medical-Intelligence-Platform.git
cd Advanced-AI-Medical-Intelligence-Platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run FastAPI

```bash
python -m uvicorn backend.app:app --reload
```

FastAPI will start at:

```
http://127.0.0.1:8000
```

---

## ▶️ Run Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

Streamlit will start at:

```
http://localhost:8501
```

---

## 🧠 Model Architecture

- Conv2D
- Batch Normalization
- MaxPooling2D
- Conv2D
- Batch Normalization
- MaxPooling2D
- Conv2D
- Batch Normalization
- MaxPooling2D
- Flatten
- Dense (256)
- Dropout
- Output Layer (Sigmoid)

---

## 🔄 Workflow

1. Upload Chest X-ray image
2. Image preprocessing
3. CNN model prediction
4. Display prediction and confidence score
5. Generate AI-assisted medical report
6. Display results through Streamlit interface

---

## 📊 Output

The application provides:

- Disease Prediction
- Prediction Confidence
- AI Medical Report

---

## 🔮 Future Improvements

- Explainable AI (Grad-CAM)
- Database for prediction history
- User authentication
- Cloud deployment
- Multi-disease detection

---

## ⚠️ Disclaimer

This application is developed for educational and research purposes only. It should not be used as a substitute for professional medical diagnosis or treatment.

---

## 👨‍💻 Author

**Uday Kiran Bhushamoni**

- Email: udaykiranbhushamoni@gmail.com
- GitHub:https://github.com/Udaykiran2252/Advanced-AI-Medical-Intelligence-Platform/edit/main/README.md
