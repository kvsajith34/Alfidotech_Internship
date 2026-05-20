# 🚀 Alfido Tech DevOps Internship

<div align="center">

![DevOps](https://img.shields.io/badge/Internship-Alfido%20Tech-blue?style=for-the-badge)
![Domain](https://img.shields.io/badge/Domain-DevOps-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-green?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-29.4.3-blue?style=for-the-badge&logo=docker)
![Terraform](https://img.shields.io/badge/Terraform-1.15.3-purple?style=for-the-badge&logo=terraform)
![Prometheus](https://img.shields.io/badge/Prometheus-2.48.0-red?style=for-the-badge&logo=prometheus)

**Intern:** Venkata Sai Ajith Kancheti &nbsp;|&nbsp; **GitHub:** [@kvsajith34](https://github.com/kvsajith34)

</div>

---

## 📋 Overview

This repository contains all tasks completed as part of the **Alfido Tech DevOps Internship** program. The projects cover core DevOps and MLOps practices including containerization, infrastructure as code, CI/CD pipelines, monitoring, logging, and incident response — all tailored to AI/ML workflows using Python.

---

## 🗂️ Repository Structure

```
Alfidotech_Internship/
├── task1-docker-webapp/                        # Task 1 — Dockerize ML Web App
├── Task2-CI_CD_Github/                         # Task 2 — CI/CD with GitHub Actions
├── Task3-IAC_terraform_basics/                 # Task 3 — Terraform IaC
└── Task4-Monitoring_Logging_incident-playbook/ # Task 4 — Monitoring & Logging
```

---

## ✅ Completed Tasks

### Task 1 — Containerize a Python ML Web App

> **Goal:** Dockerize a Flask-based ML Inference API with PostgreSQL using Docker and Docker Compose.

| Property | Detail |
|----------|--------|
| Language | Python 3.11 |
| Framework | Flask + Gunicorn |
| Database | PostgreSQL 15 |
| Model | Iris Classifier (RandomForest) |
| Build | Multi-stage Dockerfile |
| Orchestration | Docker Compose |

**Key Features:**
- Multi-stage Dockerfile (builder + runner stages)
- Flask REST API with `/`, `/health`, `/predict`, `/db` endpoints
- PostgreSQL integration via docker-compose
- Environment variable configuration

**Endpoints:**

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage |
| `/health` | GET | Health check |
| `/predict` | POST | ML prediction |
| `/db` | GET | DB connection test |

**Quick Start:**
```bash
cd task1-docker-webapp
docker compose up --build
curl http://localhost:5000/health
```

📄 [View PDF Documentation](task1-docker-webapp/Task1_Docker_Webapp_KVSajith34.pdf)

---

### Task 2 — CI/CD Pipeline with GitHub Actions *(Substitute)*

> **Goal:** Automate build, test, and deployment of ML Inference API using GitHub Actions.

| Property | Detail |
|----------|--------|
| Pipeline | GitHub Actions |
| Model | Iris Classifier (scikit-learn) |
| Tests | pytest (model + API) |
| Registry | Docker Hub (ajith72) |
| Image | ajith72/ml-inference-api |

**Pipeline Stages:**
```
Push to main → Install deps → Train model → Run pytest → Build Docker → Push to Docker Hub
```

**Note:** Workflow file exists at `.github/workflows/ci-cd.yml`. GitHub Actions integration pending due to repository path configuration.

---

### Task 3 — Infrastructure as Code with Terraform

> **Goal:** Provision ML infrastructure using Terraform with LocalStack (AWS simulation).

| Property | Detail |
|----------|--------|
| IaC Tool | Terraform v1.15.3 |
| Provider | AWS (hashicorp/aws v5.100.0) |
| Simulation | LocalStack 3.0.0 |
| Resources | 3 S3 Buckets + Versioning |

**Resources Provisioned:**

| Resource | Name | Purpose |
|----------|------|---------|
| S3 Bucket | alfido-ml-datasets-dev | ML training datasets |
| S3 Bucket | alfido-ml-models-dev | Model artifacts & checkpoints |
| S3 Bucket | alfido-ml-logs-dev | Training logs & metrics |
| S3 Versioning | ml-models-dev | Model version control |

**Commands:**
```bash
cd Task3-IAC_terraform_basics
terraform init
terraform plan
terraform apply -auto-approve
terraform state list
terraform output
```

📄 [View PDF Documentation](Task3-IAC_terraform_basics/Task3_Terraform_IaC_KVSajith34.pdf)

---

### Task 4 — Monitoring, Logging & Incident Playbook

> **Goal:** Implement advanced monitoring for the ML Inference API using Prometheus, Grafana, and Node Exporter with a complete incident runbook.

| Property | Detail |
|----------|--------|
| Metrics | Prometheus v2.48.0 |
| Visualization | Grafana v10.2.0 |
| System Metrics | Node Exporter v1.7.0 |
| Instrumentation | prometheus-client 0.20.0 |
| Alert Rules | 4 custom ML alerts |
| Dashboard Panels | 6 Grafana panels |

**Custom ML Metrics:**

| Metric | Type | Description |
|--------|------|-------------|
| `ml_request_total` | Counter | Requests by endpoint/status |
| `ml_prediction_total` | Counter | Predictions by class label |
| `ml_request_latency_seconds` | Histogram | Latency with P95 buckets |
| `ml_prediction_confidence` | Gauge | Confidence score (0–1) |
| `ml_error_total` | Counter | Errors by type |
| `ml_model_loaded` | Gauge | Model status (1=loaded) |
| `ml_active_requests` | Gauge | In-flight requests |

**Alert Rules:**

| Alert | Severity | Condition |
|-------|----------|-----------|
| `MLAPIDown` | 🔴 Critical | API unreachable > 30s |
| `HighErrorRate` | 🟡 Warning | Error rate > 0.1/s over 5m |
| `HighRequestLatency` | 🟡 Warning | P95 latency > 500ms |
| `LowPredictionConfidence` | 🟡 Warning | Confidence < 0.7 |

**Grafana Dashboard Panels:**
1. Total Predictions — Stat
2. Predictions by Class — Pie Chart
3. Request Rate — Time Series
4. P95 Request Latency — Time Series
5. Model Confidence Score — Gauge
6. Model Status — Stat (ONLINE/OFFLINE)

**Quick Start:**
```bash
cd Task4-Monitoring_Logging_incident-playbook
docker compose up --build -d

# Generate test traffic
for i in {1..30}; do
  curl -s -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"features": [5.1, 3.5, 1.4, 0.2]}' > /dev/null
done

# Access services
# ML API      → http://localhost:5000
# Prometheus  → http://localhost:9090
# Grafana     → http://localhost:3000 (admin / alfido123)
```

📄 [View Monitoring Report](Task4-Monitoring_Logging_incident-playbook/Task4_Monitoring_Logging_KVSajith34.pdf)
📄 [View Incident Runbook](Task4-Monitoring_Logging_incident-playbook/Task4_Incident_Runbook_KVSajith34.pdf)

---

## 🛠️ Tech Stack

<div align="center">

| Category | Tools |
|----------|-------|
| Language | Python 3.11 |
| ML Framework | scikit-learn, Flask |
| Containerization | Docker, Docker Compose |
| IaC | Terraform, LocalStack |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus, Grafana, Node Exporter |
| Version Control | Git, GitHub |
| OS Environment | WSL2 Ubuntu on Windows 11 |

</div>

---

## 🌐 Services & Ports

| Service | Port | Purpose |
|---------|------|---------|
| ML Inference API | 5000 | Flask prediction endpoint |
| Prometheus | 9090 | Metrics collection |
| Grafana | 3000 | Dashboards & visualization |
| Node Exporter | 9100 | System metrics |
| PostgreSQL | 5432 | Database (Task 1) |
| LocalStack | 4566 | AWS simulation (Task 3) |

---

## 📁 Documentation

All tasks include PDF submission documents with:
- Task objectives and overview
- Configuration files and code
- Build & run commands
- Screenshots of running services
- Deliverables checklist

| Task | PDF Report | Additional |
|------|-----------|------------|
| Task 1 | Task1_Docker_Webapp_KVSajith34.pdf | — |
| Task 3 | Task3_Terraform_IaC_KVSajith34.pdf | — |
| Task 4 | Task4_Monitoring_Logging_KVSajith34.pdf | Task4_Incident_Runbook_KVSajith34.pdf |

---

## 🚦 Task Completion Status

```
[✅] Beginner Tasks  — Linux, Bash Scripts, Docker basics, GitHub setup
[✅] Task 1          — Dockerize Flask ML App (Flask + PostgreSQL)
[🔄] Task 2          — CI/CD Pipeline (GitHub Actions — substitute)
[✅] Task 3          — Terraform IaC (LocalStack AWS simulation)
[✅] Task 4          — Monitoring, Logging & Incident Playbook
```

---

## 👨‍💻 About

**Venkata Sai Ajith Kancheti**
DevOps Intern — Alfido Tech
GitHub: [@kvsajith34](https://github.com/kvsajith34)

> *AIML student with a focus on MLOps, DevOps automation, and cloud-native infrastructure.*

---

<div align="center">

**Alfido Tech DevOps Internship** &nbsp;|&nbsp; 2026

</div>
