[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - CodeBuild Project last invoked greater than 90 days

--

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
| action | "codebuild_invoke_limit" | 
| project_name | CodeBuild project name |

## Remediation Execution

Following command need to execute

```sh
ansible-playbook playbook.yaml -e '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx",
  "action": "codebuild_invoke_limit",
  "project_name": "xxxx",
}'
```
