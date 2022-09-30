[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if S3 Glacier vaults have policies which allow access to everyone

The Amazon S3 Glacier storage classes are purpose-built for data archiving, providing you with the highest performance, most retrieval flexibility, and the lowest cost archive storage in the cloud. All S3 Glacier storage classes provide virtually unlimited scalability and are designed for 99.999999999% (11 nines) of data durability. The S3 Glacier storage classes deliver options for the fastest access to your archive data and the lowest-cost archive storage in the cloud.


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
| vault_policy | Policy for vault |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "region": "XXXXX",
  "vault_name": "XXXXXXXX",
  "aws_account_id":"xxxxxx",
  "vault_policy": {
    "Version":"2012-10-17",
    "Statement":[{
        "Sid":"cross-account-upload",
        "Effect":"Allow",
        "Principal":{"AWS":"*"},
        "Action":[
            "glacier:UploadArchive","glacier:InitiateMultipartUpload","glacier:AbortMultipartUpload","glacier:CompleteMultipartUpload"
        ],
        "Resource":"arn:aws:glacier:<REGION>:<ACCOUNT>:vaults/XXXXX"
    }]
   }
}'
```
