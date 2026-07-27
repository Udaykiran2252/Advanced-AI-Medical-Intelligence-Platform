import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# -----------------------------
# Load the trained model
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "pneumonia_model.keras")

print("Loading model from:", MODEL_PATH)

model = load_model(MODEL_PATH)

IMG_SIZE = (224, 224)

# -----------------------------
# Prediction Function
# -----------------------------
def predict_image(img_path):
    # Load and preprocess image
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    prediction = model.predict(img, verbose=0)[0][0]

    if prediction >= 0.5:
        label = "PNEUMONIA"
        confidence = prediction
    else:
        label = "NORMAL"
        confidence = 1 - prediction

    return {
        "prediction": label,
        "confidence": round(float(confidence) * 100, 2)
    }