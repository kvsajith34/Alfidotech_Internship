output "ml_datasets_bucket" {
  description = "S3 bucket for ML datasets"
  value       = aws_s3_bucket.ml_datasets.bucket
}

output "ml_models_bucket" {
  description = "S3 bucket for model artifacts"
  value       = aws_s3_bucket.ml_models.bucket
}

output "ml_logs_bucket" {
  description = "S3 bucket for training logs"
  value       = aws_s3_bucket.ml_logs.bucket
}

output "models_versioning_status" {
  description = "Versioning status of models bucket"
  value       = aws_s3_bucket_versioning.ml_models_versioning.versioning_configuration[0].status
}
