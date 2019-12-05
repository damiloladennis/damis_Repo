output "PublicIp" {
  value = "${aws_instance.testec2.public_ip}"
}

output "PrivateIp" {
  value = "${aws_instance.testec2.private_ip}"
}