variable "user_names" {
  description = "Create IAM Users with the names"
  type = list(string)
  default = ["mark","luke","john"]
}