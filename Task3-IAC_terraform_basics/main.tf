terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = var.aws_region
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  s3_use_path_style           = true

  endpoints {
    s3  = var.localstack_endpoint
    iam = var.localstack_endpoint
  }
}

# S3 Bucket — ML Datasets
resource "aws_s3_bucket" "ml_datasets" {
  bucket = "${var.project_name}-datasets-${var.environment}"

  tags = {
    Name        = "ML Datasets Bucket"
    Environment = var.environment
    Project     = var.project_name
    Purpose     = "Store raw and processed ML training data"
  }
}

# S3 Bucket — Model Artifacts
resource "aws_s3_bucket" "ml_models" {
  bucket = "${var.project_name}-models-${var.environment}"

  tags = {
    Name        = "ML Models Bucket"
    Environment = var.environment
    Project     = var.project_name
    Purpose     = "Store trained model artifacts and checkpoints"
  }
}

# S3 Bucket — Training Logs
resource "aws_s3_bucket" "ml_logs" {
  bucket = "${var.project_name}-logs-${var.environment}"

  tags = {
    Name        = "ML Training Logs Bucket"
    Environment = var.environment
    Project     = var.project_name
    Purpose     = "Store model training logs and metrics"
  }
}

# Enable versioning on models bucket
resource "aws_s3_bucket_versioning" "ml_models_versioning" {
  bucket = aws_s3_bucket.ml_models.id

  versioning_configuration {
    status = "Enabled"
  }
}
