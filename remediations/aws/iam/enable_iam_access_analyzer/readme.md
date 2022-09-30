[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if IAM Access Analyzer is enabled and its findings

Check for Amazon IAM Access Analyzer findings in order to review and take all the necessary actions to resolve public or untrusted cross-account access security issues identified within your Amazon Web Services (AWS) cloud environment. Access Analyzer is a new AWS Identity and Access Management (IAM) feature that helps you find potential security risks in your AWS environment by analyzing the resource-based policies associated with the cloud resources within your zone of trust.

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
| analyzer_type | Type of analyzer|
| analyzer_name | Name of the analyzer |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "aws_region": "xxxx",
  "analyzer_type": "ACCOUNT/ORGANIZATION",
  "analyzer_name": "xxxx"
}'
```