from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.getenv("MODEL_PATH", "app/model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

CLASSES = ["setosa", "versicolor", "virginica"]

@app.route("/")
def home():
    return jsonify({
        "service": "ML Inference API",
        "model": "Iris Classifier (RandomForest)",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].max()
        return jsonify({
            "prediction": CLASSES[prediction],
            "confidence": round(float(probability), 4)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
