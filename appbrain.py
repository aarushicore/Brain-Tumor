from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = load_model('model/mobilenetv2_model.h5')

# Class names (you must match this with the model's output order)
class_names = ['Glioma Tumor', 'Meningioma Tumor', 'No Tumor', 'Pituitary Tumor']

# Preprocess function
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Match model input
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/', methods=['GET', 'POST'])
def upload_predict():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(filepath)
            img = preprocess_image(filepath)
            prediction = model.predict(img)
            predicted_class_index = np.argmax(prediction)
            predicted_class_name = class_names[predicted_class_index]
            confidence = np.max(prediction) * 100
            result = f"{predicted_class_name} ({confidence:.2f}%)"
            return render_template('index.html', prediction=result, image_loc=filepath)
    return render_template('index.html', prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
    