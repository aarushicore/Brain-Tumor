# Brain Tumor Classification Web App 🧠

This is a Flask-based web application that allows users to upload MRI brain scan images and get predictions for four types of brain conditions using a deep learning model based on MobileNetV2.

## 🔍 Project Overview

The model classifies uploaded MRI images into one of the following categories:

- Glioma Tumor
- Meningioma Tumor
- No Tumor
- Pituitary Tumor

## 📁 Project Structure

├── appbrain.py # Flask application
├── model/
│ └── mobilenetv2_model.h5 # Pre-trained Keras model
├── static/
│ └── uploads/ # Directory to store uploaded images
├── templates/
│ └── index.html # Frontend template for user interaction
└── README.md # Project documentation

bash
Copy
Edit

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/brain-tumor-classifier.git
cd brain-tumor-classifier
2. Install dependencies
It is recommended to use a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Make sure requirements.txt includes:

nginx
Copy
Edit
Flask
tensorflow
opencv-python
numpy
3. Run the application
bash
Copy
Edit
python appbrain.py
Then visit http://127.0.0.1:5000/ in your web browser.

📸 Example
Upload an MRI scan image and get instant classification results like:

java
Copy
Edit
Predicted: Glioma Tumor (92.34%)
💡 Notes
Ensure that mobilenetv2_model.h5 is present in the model/ directory.

The uploaded images are saved in the static/uploads/ folder.

The model input size is (224, 224).

📌 To Do
Add user authentication

Improve frontend UI

Add support for batch predictions

Dockerize the app

📜 License
This project is licensed under the MIT License.
