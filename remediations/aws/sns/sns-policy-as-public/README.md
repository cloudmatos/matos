
[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if SNS topics have policy set as Public
AWS SNS is a hosted topics service that lets you integrate distributed software systems and components. It provides a generic web services API and it can be accessed by any programming language that the AWS SDK supports.
Public SNS topics potentially expose existing interfaces to unwanted 3rd parties that can tap into an existing data stream, resulting in data leak to an unwanted party.


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
| sns_topic      | SNS Topic Name  |



## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx",
  "sns_topic":"xxxx"
}'
```
