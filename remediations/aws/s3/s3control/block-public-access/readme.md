[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check S3 Account Level Public Access Block

Ensure that Amazon S3 Block Public Access feature is enabled for your AWS account to restrict public access to all your S3 buckets, including those that you create in the future. This feature has the ability to override existing policies and permissions in order to block S3 public access and to make sure that this type of access is not granted to newly created buckets and object

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
| region | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region |
| vault_name | Name of the vault. |
| aws_account_id | AWS Account Number |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "region": "XXXXX",
  "vault_name": "XXXXXXXX",
  "aws_account_id":"xxxxxx"
}'
```