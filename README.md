# Brain Tumor Detection using MobileNetV2 (Flask Web App)

This is a sub-project of the [Multi Disease Prediction](https://github.com/deoprakash/multi_disease_prediction) system. It provides a simple web interface to detect brain tumors using a pre-trained MobileNetV2 deep learning model.

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


git clone https://github.com/AryaSingh-25/brain-tumor.git
cd brain-tumor

2. (Optional but recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the Flask app:

python appbrain.py

5. Open your browser and go to:

http://127.0.0.1:5000

🧪 Model Details
Architecture: MobileNetV2
Input size: 224x224
Output: 4 classes
File: mobilenetv2_model.h5 (should be <100MB to be hosted on GitHub)

📸 Usage
Upload a brain MRI image via the web interface.
The model predicts the class of tumor (or no tumor, with 4 subclasses).
The result and confidence are displayed on the same page.

🧩 Part of Larger Project
This is a modular part of the Multi Disease Prediction Project, which aims to detect various diseases using deep learning models and a unified interface.

📜 License
MIT License (or specify your license)
