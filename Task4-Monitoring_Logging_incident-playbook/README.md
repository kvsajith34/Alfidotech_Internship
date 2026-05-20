# Task 4 — Monitoring, Logging & Incident Playbook

**Intern:** KVSajith34  
**Internship:** Alfido Tech — DevOps Track  
**Task:** Implement monitoring and logging for ML Inference API

---

## Overview

Advanced monitoring stack for the Iris Classification ML API using
Prometheus, Grafana, and Node Exporter. Includes 7 custom ML metrics,
4 alert rules, 6 Grafana dashboard panels, and a full incident runbook.

---

## Architecture
Flask ML API → /metrics → Prometheus → Grafana Dashboard
→ Alert Rules
Node Exporter → system metrics → Prometheus
---

## Services

| Service | Port | Purpose |
|---------|------|---------|
| ML Inference API | 5000 | Flask + Prometheus metrics |
| Prometheus | 9090 | Metrics collection & alerting |
| Grafana | 3000 | Dashboards & visualization |
| Node Exporter | 9100 | System metrics |

---

## Custom ML Metrics

| Metric | Type | Description |
|--------|------|-------------|
| ml_request_total | Counter | Requests by endpoint/status |
| ml_prediction_total | Counter | Predictions by class |
| ml_request_latency_seconds | Histogram | Latency with P95 buckets |
| ml_prediction_confidence | Gauge | Confidence score (0-1) |
| ml_error_total | Counter | Errors by type |
| ml_model_loaded | Gauge | Model status (1=loaded) |
| ml_active_requests | Gauge | In-flight requests |

---

## Alert Rules

| Alert | Severity | Condition |
|-------|----------|-----------|
| MLAPIDown | Critical | API unreachable > 30s |
| HighErrorRate | Warning | Error rate > 0.1/s |
| HighRequestLatency | Warning | P95 latency > 500ms |
| LowPredictionConfidence | Warning | Confidence < 0.7 |

---

## Grafana Dashboard Panels

1. Total Predictions — Stat
2. Predictions by Class — Pie Chart
3. Request Rate — Time Series
4. P95 Request Latency — Time Series
5. Model Confidence Score — Gauge
6. Model Status — Stat (ONLINE/OFFLINE)

---

## Project Structure
task4-monitoring/
├── app/
│   ├── app.py               # Flask API + Prometheus metrics
│   ├── train.py             # Model training
│   └── requirements.txt
├── prometheus/
│   ├── prometheus.yml       # Scrape config
│   └── alert_rules.yml      # ML alert rules
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── datasource.yml
│       └── dashboards/
│           └── dashboard.yml
├── Dockerfile
├── docker-compose.yml
└── README.md
---

## Quick Start

```bash
# Start all services
docker compose up --build -d

# Verify services
docker ps

# Generate test traffic
for i in {1..30}; do
  curl -s -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{"features": [5.1, 3.5, 1.4, 0.2]}' > /dev/null
done

# Check metrics
curl http://localhost:5000/metrics | grep ml_

# Stop services
docker compose down
```

---

## Access URLs

| Service | URL | Credentials |
|---------|-----|-------------|
| ML API | http://localhost:5000 | — |
| Prometheus | http://localhost:9090 | — |
| Grafana | http://localhost:3000 | admin / alfido123 |

---

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| / | GET | Service info |
| /health | GET | Health check |
| /predict | POST | ML prediction |
| /metrics | GET | Prometheus metrics |
| /stats | GET | Model statistics |

---

## Sample Prediction

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

**Response:**
```json
{
  "prediction": "setosa",
  "confidence": 1.0,
  "probabilities": {
    "setosa": 1.0,
    "versicolor": 0.0,
    "virginica": 0.0
  },
  "latency_ms": 2.45
}
```

---

## Deliverables

- `Task4_Monitoring_Logging_KVSajith34.pdf` — Full report
- `Task4_Incident_Runbook_KVSajith34.pdf` — Incident playbook

---

## Tools Used

- Python 3.11 + Flask
- Prometheus v2.48.0
- Grafana v10.2.0
- Node Exporter v1.7.0
- Docker + Docker Compose
- WSL2 Ubuntu on Windows 11
