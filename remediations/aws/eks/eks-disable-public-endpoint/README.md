[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Ensure EKS Clusters are created with Private Endpoint Enabled and Public Access Disabled

Ensure that your Amazon EKS cluster's Kubernetes API server endpoint is not publicly accessible from the Internet in order to avoid exposing private data and minimizing security risks. The level of access to your Kubernetes API server endpoints depends on your EKS application use cases, however, for most use cases Cloud Conformity recommends that the API server endpoints should be accessible only from within your AWS Virtual Private Cloud (VPC).

> Remediation Tool   - [Ansible](https://www.ansible.com/)

> Remediation Script - [playbook.yml](playbook.yml)

## Remediation Requirements
The below requirements are needed to execute remediation script

> pip packages
- python >= 3.6
- boto3 >= 1.15.0
- botocore >= 1.18.0

## Remediation Parameters

| Parameter | Comments |
| ------ | ------ |
| aws_access_key | AWS Access key |
| aws_secret_key | AWS Secret key |
| aws_region | AWS Region |
| action | "eks_disable_public_endpoint" | 
| eks_cluster_name | EKS cluster name |

## Remediation Execution

Following command need to execute

```sh
ansible-playbook playbook.yaml -e '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx",
  "action": "eks_disable_public_endpoint",
  "eks_cluster_name": "xxxx",
}'
```
