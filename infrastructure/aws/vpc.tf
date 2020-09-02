module "vpc" {
    source = "terraform-aws-modules/vpc/aws"
    version = "~> v2.0"

    name = var.project
    cidr = var.vpc_cidr

    azs             = data.aws_availability_zones.available.names
    private_subnets = var.priv_cidr_block
    public_subnets  = var.pub_cidr_block

    enable_nat_gateway = true
    enable_dns_support = true

    public_subnet_tags = {
        "kubernetes.io/cluster/${var.project}" = "shared"
        "kubernetes.io/role/elb"                      = "1"
    }

    private_subnet_tags = {
        "kubernetes.io/cluster/${var.project}" = "shared"
        "kubernetes.io/role/internal-elb"             = "1"
    }

    tags = var.tags
}