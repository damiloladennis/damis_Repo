variable "region" {
  default = "us-east-1"
}
variable "accesskey" {
  type =  "string"
}
variable "secretkey" {
  type = "string"
}
variable "imageid" {
  default = "ami-00d4e9ff62bc40e03"
}
variable "keyname" {
  default = "terraform"
}
variable "securitygroups" {
  default = ["allow_all"]
}
variable "instancetype" {
  default = "t2.micro"
}