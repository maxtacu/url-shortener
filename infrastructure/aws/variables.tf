variable "project" {
    type = string
    description = "Project name"

    default = "url-shortener"
}

variable "vpc_cidr" {
    type = string
    default = "10.0.0.0/16"
    description = "VPC CIDR"
}

variable "tags" {
    type = map(string)
    description = "Overall tags of your resources"
    default = {
        managedby = "Terraform"
    }
}

variable "pub_cidr_block" {
    type = list(string)
    description = "Public subnets"

    default = ["10.0.0.0/19", "10.0.32.0/19", "10.0.64.0/19"]
}

variable "priv_cidr_block" {
    type = list(string)
    description = "Public subnets"  # There is also a remaining CIDR 10.0.192.0/18 with 16382 hosts available

    default = ["10.0.96.0/19", "10.0.128.0/19", "10.0.160.0/19"]
}

variable "region" {
  default = "eu-west-1"
}

variable "domain" {
  type = string
  default = "*.shortdemo.tk"

  description = "Route53 domain"
}