from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import pickle
import numpy as np
import os
import time
import logging
import json

# ── Logging Setup ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger("ml-api")

app = Flask(__name__)

# ── Load Model ────────────────────────────────────────────────
MODEL_PATH = os.getenv("MODEL_PATH", "app/model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

CLASSES = ["setosa", "versicolor", "virginica"]

# ── Prometheus Metrics ────────────────────────────────────────
REQUEST_COUNT = Counter(
    "ml_request_total",
    "Total number of requests",
    ["method", "endpoint", "status"]
)

PREDICTION_COUNT = Counter(
    "ml_prediction_total",
    "Total predictions by class",
    ["predicted_class"]
)

REQUEST_LATENCY = Histogram(
    "ml_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

CONFIDENCE_GAUGE = Gauge(
    "ml_prediction_confidence",
    "Last prediction confidence score"
)

ERROR_COUNT = Counter(
    "ml_error_total",
    "Total prediction errors",
    ["error_type"]
)

MODEL_LOAD_STATUS = Gauge(
    "ml_model_loaded",
    "Whether the ML model is loaded (1=yes, 0=no)"
)
MODEL_LOAD_STATUS.set(1)

ACTIVE_REQUESTS = Gauge(
    "ml_active_requests",
    "Number of active requests being processed"
)

# ── Routes ────────────────────────────────────────────────────
@app.route("/")
def home():
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    return jsonify({
        "service": "Alfido ML Inference API",
        "model": "Iris Classifier — RandomForest",
        "version": "1.0.0",
        "status": "running",
        "endpoints": ["/predict", "/health", "/metrics", "/stats"]
    })

@app.route("/health")
def health():
    REQUEST_COUNT.labels("GET", "/health", "200").inc()
    return jsonify({
        "status": "healthy",
        "model_loaded": True,
        "model_type": "RandomForestClassifier",
        "classes": CLASSES
    })

@app.route("/predict", methods=["POST"])
def predict():
    ACTIVE_REQUESTS.inc()
    start = time.time()
    try:
        data = request.get_json()
        if not data or "features" not in data:
            raise ValueError("Missing 'features' in request body")

        features = np.array(data["features"]).reshape(1, -1)

        if features.shape[1] != 4:
            raise ValueError(f"Expected 4 features, got {features.shape[1]}")

        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]
        confidence = float(probabilities.max())
        predicted_class = CLASSES[prediction]

        # Update metrics
        PREDICTION_COUNT.labels(predicted_class).inc()
        CONFIDENCE_GAUGE.set(confidence)
        REQUEST_COUNT.labels("POST", "/predict", "200").inc()

        latency = time.time() - start
        REQUEST_LATENCY.labels("/predict").observe(latency)

        logger.info(json.dumps({
            "event": "prediction",
            "class": predicted_class,
            "confidence": round(confidence, 4),
            "latency_ms": round(latency * 1000, 2),
            "probabilities": {
                CLASSES[i]: round(float(p), 4)
                for i, p in enumerate(probabilities)
            }
        }))

        return jsonify({
            "prediction": predicted_class,
            "confidence": round(confidence, 4),
            "probabilities": {
                CLASSES[i]: round(float(p), 4)
                for i, p in enumerate(probabilities)
            },
            "latency_ms": round(latency * 1000, 2)
        })

    except ValueError as e:
        ERROR_COUNT.labels("validation_error").inc()
        REQUEST_COUNT.labels("POST", "/predict", "400").inc()
        logger.error(json.dumps({"event": "error", "type": "validation", "detail": str(e)}))
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        ERROR_COUNT.labels("server_error").inc()
        REQUEST_COUNT.labels("POST", "/predict", "500").inc()
        logger.error(json.dumps({"event": "error", "type": "server", "detail": str(e)}))
        return jsonify({"error": "Internal server error"}), 500

    finally:
        ACTIVE_REQUESTS.dec()

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

@app.route("/stats")
def stats():
    REQUEST_COUNT.labels("GET", "/stats", "200").inc()
    return jsonify({
        "model": "RandomForestClassifier",
        "dataset": "Iris",
        "classes": CLASSES,
        "features": [
            "sepal_length", "sepal_width",
            "petal_length", "petal_width"
        ],
        "sample_inputs": {
            "setosa":     [5.1, 3.5, 1.4, 0.2],
            "versicolor": [6.0, 2.9, 4.5, 1.5],
            "virginica":  [6.7, 3.1, 5.6, 2.4]
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
