provider "aws" {
  region     = "${var.region}"
  access_key = "${var.accesskey}"
  secret_key = "${var.secretkey}"
}
resource "aws_instance" "testec2" {
  ami = "${var.imageid}"
  instance_type = "${var.instancetype}"
  key_name = "${var.keyname}"
  security_groups = ["${aws_security_group.allow_all.name}"]
}

resource "aws_instance" "testec3" {
  ami = "${var.imageid}"
  instance_type = "${var.instancetype}"
  key_name = "${var.keyname}"
  security_groups = "${var.securitygroups}"
}
resource "aws_security_group" "allow_all" {
  name = "allow_all"
  description = "All all inbound traffic"
  vpc_id = "${"vpc-174a066d"}"

  ingress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = [
      "0.0.0.0/0"]
  }

  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}