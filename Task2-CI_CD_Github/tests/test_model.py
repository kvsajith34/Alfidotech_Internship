import pytest
import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from app.train import train_model

def test_model_accuracy():
    """Model accuracy must be above 90%"""
    acc = train_model()
    assert acc >= 0.90, f"Accuracy {acc} is below 90%"

def test_model_prediction_shape():
    """Model must return single prediction"""
    with open("app/model.pkl", "rb") as f:
        model = pickle.load(f)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    pred = model.predict(sample)
    assert pred.shape == (1,)

def test_model_classes():
    """Model must predict valid class index (0, 1, 2)"""
    with open("app/model.pkl", "rb") as f:
        model = pickle.load(f)
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    pred = model.predict(sample)[0]
    assert pred in [0, 1, 2]
