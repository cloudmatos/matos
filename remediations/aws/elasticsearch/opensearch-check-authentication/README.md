[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check connection and authentication for Internet exposed Amazon Elasticsearch Service (ES) domains

Identify any publicly accessible AWS Elasticsearch domains and update their access policy in order to stop any unsigned requests made to these resources (ES clusters).

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
| -------------- | -------------- |
| aws_access_key | AWS Access key |
| aws_secret_key | AWS Secret key |
| aws_region | AWS Region |
| domain_name | OpenSearch Name |
| action | "opensearch_check_authentication" |

## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yaml -e '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx",
  "domain_name": "xxxx", 
  "action": "opensearch_check_authentication"
}'
```
