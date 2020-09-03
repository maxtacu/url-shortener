## Requirements

| Name | Version |
|------|---------|
| terraform | >= 0.12.0 |
| aws | ~> 3.0 |
| kubernetes | ~> 1.11 |

## Providers

| Name | Version |
|------|---------|
| aws | ~> 3.0 |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| domain | Route53 domain | `string` | `"*.shortdemo.tk"` | no |
| priv\_cidr\_block | Public subnets | `list(string)` | <pre>[<br>  "10.0.96.0/19",<br>  "10.0.128.0/19",<br>  "10.0.160.0/19"<br>]</pre> | no |
| project | Project name | `string` | `"url-shortener"` | no |
| pub\_cidr\_block | Public subnets | `list(string)` | <pre>[<br>  "10.0.0.0/19",<br>  "10.0.32.0/19",<br>  "10.0.64.0/19"<br>]</pre> | no |
| region | n/a | `string` | `"eu-west-1"` | no |
| tags | Overall tags of your resources | `map(string)` | <pre>{<br>  "managedby": "Terraform"<br>}</pre> | no |
| vpc\_cidr | VPC CIDR | `string` | `"10.0.0.0/16"` | no |

## Outputs

No output.

