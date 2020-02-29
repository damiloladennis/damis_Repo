#! /bin/bash

#getting sudo previdleges
sudo su

# installing apache 2
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service

# Helow world from hostname to index.html file
