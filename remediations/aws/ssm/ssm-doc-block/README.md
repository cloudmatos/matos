
[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if there are SSM Documents set as public
Unless your use case requires public sharing to be turned on, we recommend turning on the block public sharing setting for your AWS Systems Manager (SSM) documents. Turning on this setting prevents unwanted access to your SSM documents. The block public sharing setting is an account level setting that can differ for each AWS Region

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

## Remediation Execution

Following command need to execute

```sh
ansible-playbook playbook.yaml -e '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx"
}'
```
