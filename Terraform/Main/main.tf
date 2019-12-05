provider "aws" {
 region     = "${var.region}"
 access_key = "${var.accesskey}"
 secret_key = "${var.secretkey}"
}

resource "aws_security_group" "allow_all" {
  name = "allow_all"
  description = "All all inbound traffic"
  vpc_id = "${var.vpcid}"

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
resource "aws_instance" "appserver1" {
  ami            = "${var.imageid}"
  instance_type  = "${var.instancetype}"
  key_name       = "${var.key}"
  security_groups = ["${aws_security_group.allow_all.name}"]

  connection {
    user = "ubuntu"
    host = self.public_ip
    private_key = "${file(var.privatekeypath)}"
  }
  provisioner "remote-exec" {
    inline = [
    "sudo apt-get update",
    "sudo apt-get install tomcat7 -y",
    ]
  }

}



