# Brain Tumor Detection using MobileNetV2 (Flask Web App)

This is a sub-project of the [Multi Disease Prediction](https://github.com/deoprakash/multi_disease_prediction) system. It provides a simple web interface to detect brain tumors using a pre-trained MobileNetV2 deep learning model.

deployment on hugging face: https://huggingface.co/spaces/aryasingh1320/brain-tumor-detector

## 🧠 Overview

This web app allows users to upload MRI brain images and predicts whether the image indicates:

- Glioma Tumor
- Meningioma Tumor
- Pituitary Tumor
- No Tumor

The model is built using **MobileNetV2** and wrapped in a **Flask** web application.

---

## 🗂️ Project Structure
brain-tumor/ ├── appbrain.py # Flask app ├── requirements.txt # Python dependencies ├── model/ │ └── mobilenetv2_model.h5 # Pre-trained Keras model ├── static/ │ └── uploads/ # Uploaded images folder ├── templates/ │ └── index.html # Web interface template └── .gitignore # Files/folders to ignore in Git

---

## 🚀 How to Run

1. **Clone this repository:**

```bash
git clone https://github.com/AryaSingh-25/brain-tumor.git
cd brain-tumor
