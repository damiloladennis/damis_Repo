provider "aws" {
  region = "${var.region}"
  shared_credentials_file = "${var.shared_credentials_file}"
  profile = "${var.profile}"
}

resource "aws_s3_bucket" "damiterraformstate" {
  bucket = "${var.bucket}"
  versioning {
    enabled = false
  }
  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}

resource "aws_dynamodb_table" "damiterraformlocks" {
  name         = "damiterraformlocks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}
resource "aws_instance" "example" {
  ami           = "${var.ami}"
  instance_type = "${var.instancetype}"
}








