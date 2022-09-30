[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check exposed KMS keys
KMS keys are used for encrypting and decrypting data which may be sensitive. Publicly accessible KMS keys may allow anyone to perform decryption operations which may reveal data.

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
| key_id | id of kms key |
| key_policy | policy for kms key |

## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "aws_region": "xxxx",
  "key_id":"xxxxx",
  "key_policy":{
    "Id":"xxxx",
    "Version":"xxxx",
    "Statement":[{
        "Sid":"xxx",
        "Effect":"Allow",
        "Principal":{
            "AWS":"arn:aws:iam::xxxx:<user>"
            },
        "Action":"kms:*",
        "Resource":"*"
        }]
    },
    "account_id":"xxxxx"
}'
```