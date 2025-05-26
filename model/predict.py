import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import argparse
import os

def load_model():
    return tf.keras.models.load_model("model/trend_pattern_model.h5")

def predict(image_path):
    model = load_model()
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)
    class_idx = np.argmax(preds)
    class_labels = sorted(os.listdir("images"))
    print(f"Prediction: {class_labels[class_idx]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to candlestick chart image")
    args = parser.parse_args()
    predict(args.image)
