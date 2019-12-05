variable "region" {
  default = "us-east-1"
}
variable "shared_credentials_file" {
  default = "/Users/user/.aws/credentials"
}
variable "profile" {
  default = "DevOps"
}
variable "bucket" {
  default = "damiterraformstate"
}
variable "dynamodb_table" {
  default = "damiterraformlocks"
}
variable "ami" {
  default = "ami-04b9e92b5572fa0d1"
}
variable "instancetype" {
  default = "t2.micro"
}
variable "key" {
  default = "global/s3/terraform.tfstate"
}