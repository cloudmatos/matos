[<img src="https://github.com/cloudmatos/matos/blob/master/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check if any of the Elastic or Public IP are in Shodan 

Shodan is a search engine for Internet connected devices, ranging from internet connected cameras to cloud servers.

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
| aws_access_key | AWS Access key  |
| aws_secret_key | AWS Secret key  |
| aws_region     | AWS Region Name |
| instance_id    | EC2 Instance Id |
| subnet_id      | Subnet Id       |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
 "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "aws_region": "xxxx",
  "instance_id": "xxx",
  "subnet_id": "xxx"
}'

