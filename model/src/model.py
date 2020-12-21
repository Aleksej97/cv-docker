from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf
from flask import Flask, request
import requests
import os

PORT = int(os.environ.get("PORT"))

EMOTIONS = ["Angriness", "Disgust", "Fear", "Happiness", "Neutral", "Sadness", "Surprise"]

# load model from JSON file
with open("model.json", "r") as file:
    json_model = file.read()
    model = model_from_json(json_model)

# load weights into the new model
model.load_weights("model_weights.h5")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict_emotion():
    data = request.json
    img = np.array(data['image'])
    predictions = model.predict(img)
    return EMOTIONS[np.argmax(predictions)]


if __name__ == '__main__':
    app.run('0.0.0.0', port=PORT)
