[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Ensure there are no ECR repositories set as Public
AWS ECR is a managed Docker registry service that simplifies Docker container image management. The ECR repository is a collection of Docker images available on AWS. Access control to ECR repositories is governed using resource-based policies. A public ECR repository can expose internal Docker images that contain confidential business logic.

We recommend you do not allow unrestricted public access to ECR repositories to help avoid data leakage.

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
| aws_region | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region |
| ecr_repo | name of the ecr repo |


## Remediation Execution
Following command need to execute
```sh

ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "aws_region": "XXXXX",
  "ecr_repo":"xxxxx"
}'
```

