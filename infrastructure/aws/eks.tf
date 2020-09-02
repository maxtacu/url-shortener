data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_id
}

module "eks" {
    source          = "terraform-aws-modules/eks/aws"
    cluster_name    = var.project
    cluster_version = "1.17"
    subnets         = module.vpc.private_subnets

    tags = var.tags

    vpc_id = module.vpc.vpc_id

    worker_groups = [
        {
            name                          = "worker-group-1"
            instance_type                 = "t2.small"
            asg_desired_capacity          = 2
            key_name                      = aws_key_pair.maxkeypair.key_name
            additional_security_group_ids = [aws_security_group.worker_group_vpc.id]
        }
    ]

    worker_additional_security_group_ids = [aws_security_group.home_access.id, aws_security_group.instance_alb.id]

}