# Task 3 — Infrastructure as Code with Terraform

**Intern:** KVS Ajith
**Internship:** Alfido Tech — DevOps Track  
**Task:** Provision ML infrastructure using Terraform + LocalStack

---

## Overview

Terraform configuration to provision AWS S3 infrastructure
for an ML pipeline, simulated locally using LocalStack.

---

## Infrastructure Provisioned

| Resource | Name | Purpose |
|----------|------|---------|
| S3 Bucket | alfido-ml-datasets-dev | ML training datasets |
| S3 Bucket | alfido-ml-models-dev | Model artifacts & checkpoints |
| S3 Bucket | alfido-ml-logs-dev | Training logs & metrics |
| S3 Versioning | ml-models-dev | Model version control |

---

## Project Structure
task3-terraform/
├── main.tf            # Provider + resource definitions
├── variables.tf       # Input variables
├── outputs.tf         # Output values
├── terraform.tfvars   # Variable values
└── README.md
---

## State Handling

Terraform tracks all provisioned resources in `terraform.tfstate`.
This file records the current state of infrastructure and is used
to plan future changes. Never edit it manually.

---

## Variables

| Variable | Description | Default |
|----------|-------------|---------|
| aws_region | AWS region | us-east-1 |
| project_name | Resource name prefix | alfido-ml |
| environment | Deployment environment | dev |
| localstack_endpoint | LocalStack URL | http://localhost:4566 |

---

## Commands
Linux/WSL UBUNTU Commands
```bash
# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply -auto-approve

# List provisioned resources
terraform state list

# Show outputs
terraform output

# Destroy all resources
terraform destroy -auto-approve
```

---

## Tools Used

- Terraform v1.15.3
- LocalStack 3.0.0 (AWS simulation)
- Docker Desktop
- WSL2 Ubuntu
