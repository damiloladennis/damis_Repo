variable "s3_bucket_arn" {
  default = "arn:aws:s3:::damiterraformstate"
  description = "The s3_bucket_arn"
}
variable "dynamodb_table_name" {
  default = "damiterraformlocks"
  description = "The dynamodb_table_name"
}