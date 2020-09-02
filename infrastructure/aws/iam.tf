resource "aws_iam_role_policy" "eks_node_policy" {
  name   = "eks-node-policy"
  role   = module.eks.worker_iam_role_name
  policy = file("iam-nodes-policy.json")
  #  from https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html
}