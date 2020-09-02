resource "aws_security_group" "worker_group_vpc" {
  name_prefix = "worker_group_mgmt_one"
  vpc_id      = module.vpc.vpc_id

  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"

    cidr_blocks = list(var.vpc_cidr)
  }
}

resource "aws_security_group" "home_access" {
  name_prefix = "worker_group_mgmt_one"
  vpc_id      = module.vpc.vpc_id

  ingress {
    from_port = 22
    to_port   = 22
    protocol  = "tcp"

    cidr_blocks = ["109.49.49.121/32"]
  }
}

resource "aws_security_group" "alb" {
  name        = "${var.project}-alb-sg"
  vpc_id      = module.vpc.vpc_id
  description = "ALB ${var.project}"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.tags,
    {
      "Name"  = "${var.project}-alb-sg"
    }
  )
}

resource "aws_security_group" "instance_alb" {
  name        = "${var.project}-instance_alb-sg"
  vpc_id      = module.vpc.vpc_id
  description = "${var.project} ALB to Instance SG"

  ingress {
    from_port       = 0
    to_port         = 65535
    protocol        = "TCP"
    security_groups = [aws_security_group.alb.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = var.tags
}