[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Check if Security Hub is enabled and its standard subscriptions

A Security Hub standard, such as CIS AWS Foundations standard, is a predefined collection of rules based on the AWS cloud and industry best practices. Once the Security Hub service is enabled, it immediately begins running continuous and automated checks on your AWS environment's resources against the rules included in the active standards. Then AWS Security Hub generates findings based on the results of the checks defined within the enabled standards. Even if these standards help you adhere to industry (including AWS) best practices, there can be scenarios where specific security standards are not needed or are considered unwanted due to regulatory requirements that these promote, or where these need to be disabled to lower the cost of the monthly AWS bill as standards rules use the configuration items recorded by AWS Config, therefore Config service charges apply.

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

## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yaml -e '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx"
}'
```
