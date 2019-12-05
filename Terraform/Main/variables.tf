variable "region" {
  default = "us-east-1"
}

variable "accesskey" {
  type = "string"
}

variable "secretkey" {
  type = "string"
}

variable "imageid" {
  default = "ami-00d4e9ff62bc40e03"
  description = "Ubuntu 14 version"
}

variable "key" {
  default = "terraform"
}

variable "instancetype" {
  default = "t2.micro"
}

variable "vpcid" {
  default = "vpc-174a066d"
}

variable "privatekeypath" {

}