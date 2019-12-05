provider "aws" {
  region = "us-east-1"
  shared_credentials_file = "/Users/user/.aws/credentials"
  profile = "DevOps"
}

module "service" {
  source = "..//..//module//service"

  instancetype = "t2.nano"
}



