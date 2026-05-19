# Task 2 — CI/CD Pipeline for ML Inference API

[![ML App CI/CD Pipeline](https://github.com/KVSajith34/alfido-devops-internship/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/KVSajith34/alfido-devops-internship/actions/workflows/ci-cd.yml)

**Intern:** KVS Ajith
**Internship:** Alfido Tech — DevOps Track
**Task:** CI/CD Pipeline with GitHub Actions for ML Model Serving

---

## Overview

Automated CI/CD pipeline that trains, tests, and deploys
an Iris classification ML model as a Flask REST API using
GitHub Actions and Docker Hub.

---

## ML Model

| Property | Detail |
|----------|--------|
| Algorithm | Random Forest Classifier |
| Dataset | Iris (scikit-learn) |
| Accuracy | ~100% |
| Classes | setosa, versicolor, virginica |

---

## Pipeline Stages

| Stage | Description |
|-------|-------------|
| Train | Train scikit-learn model |
| Test | pytest model + API tests |
| Build | Docker multi-stage build |
| Push | Push image to Docker Hub |

---

## Project Structure
task2-ci_cd_github/
├── .github/workflows/ci-cd.yml
├── app/
│   ├── app.py
│   ├── train.py
│   └── requirements.txt
├── tests/
│   ├── test_model.py
│   └── test_api.py
├── Dockerfile
└── README.md
---

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Service info |
| `/health` | GET | Health check |
| `/predict` | POST | ML prediction |

---

## Sample Prediction

```bash
curl http://localhost:5000/predict \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

**Response:**
```json
{
  "prediction": "setosa",
  "confidence": 1.0
}
```

---

## Docker Hub
Image: ajith72/ml-inference-api:latest
## Run Locally

```bash
docker pull ajith72/ml-inference-api:latest
docker run -p 5000:5000 ajith72/ml-inference-api:latest
```