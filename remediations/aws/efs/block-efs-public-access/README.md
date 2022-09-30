
[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if EFS have policies which allow access to everyone
Amazon EFS access points are application-specific entry points into an EFS file system that make it easier to manage application access to shared datasets. Access points can enforce a user identity, including the user's POSIX groups, for all file system requests that are made through the access point. Access points can also enforce a different root directory for the file system so that clients can only access data in the specified directory or its subdirectories.
You can use Amazon Identity and Access Management (IAM) policies to enforce that specific applications use a specific access point. By combining IAM policies with access points, you can easily provide secure access to specific datasets for your applications.

> Remediation Tool   - [Ansible](https://www.ansible.com/)

> Remediation Script - [playbook.yml](playbook.yml)

## Remediation Requirements
The below requirements are needed to execute remediation script

> pip packages
- python >= 3.6
- boto3 >= 1.15.0
- botocore >= 1.18.0

## Remediation Parameters

| Parameter      | Comments        |
|----------------|-----------------|
| aws_access_key | AWS Access key  |
| aws_secret_key | AWS Secret key  |
| aws_region     | AWS Region Name |
| efs_id         | EFS ID          |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yaml --extra-vars '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxxx",
  "efs_id": "fs-xxxx",
}'
```
