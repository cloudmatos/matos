[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Restrict Access to the Control Plane Endpoint (Manual)

Amazon EKS creates an endpoint for any managed Kubernetes API server to communicate with the cluster. This API server endpoint is public to the internet by default. Access to it should be regulated using AWS IAM and native Kubernetes RBAC.

We recommended that your Kubernetes API server remains private so that all communication between worker nodes and APIs stays within your VPC. If public access is needed, restrict the IP addresses that can access your API server from the internet to reduce the potential attack surface.

> Remediation Tool - [Ansible](https://www.ansible.com/)

> Remediation Script - [playbook.yml](playbook.yml)

## Remediation Requirements
The below requirements are needed to execute remediation script

- aws cli >= 2.4.5
- python >= 3.6

## Remediation Parameters

| Parameter | Comments |
| ------ | ------ |
| aws_access_key | AWS Access Key ID  |
| aws_secret_key | AWS secret Key |
| aws_region  | AWS Region | 
| cluster_name | AWS EKS Cluster Name |
| public_access_cidrs | Name of KMS CMK Key |

## Remediation Execution

Following command need to execute

```sh
ansible-playbook playbook.yaml -e '{
   "aws_access_key": "xxx",
    "aws_secret_key": "xxx",
    "aws_region": "xxxx",
    "cluster_name": "test-remediation",
    "public_access_cidrs": ["xx.xx.xxx.xx/x"]
}'
```
