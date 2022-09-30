[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Ensure the default security group of every VPC restricts all traffic
Security groups are stateful and provide filtering of ingress/egress network traffic to AWS resources. We recommend that security groups do not allow unrestricted ingress access to port 22. Removing unfettered connectivity to remote console services, such as SSH, reduces a server's exposure to risk.

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
| security_groups | List of security groups |
| remove_all_sg_rules | True/False


## Remediation Execution
Following command need to execute
```sh

ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "security_groups":[{
    "id":"sg-xxxxx",
    "name":"xxx",
    "description":"xxxxxx"
   }],
   "remove_all_sg_rules":True
}'
```