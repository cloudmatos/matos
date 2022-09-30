[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Check for Publicly Accessible Redshift Clusters
Ensure that your redshift clusters are not exposed to the internet as this could lead to potential data loss as you are giving direct access to your clusters. This is why it is considered a security best practice and should have public access removed. 
When your Amazon Redshift clusters are publicly accessible and have a public IP address, every machine on the Internet can establish a connection to your clusters and this can increase the opportunity for malicious activity such as SQL injections or Distributed Denial of Service (DDoS) attacks.

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
| cluster_identifier | name of the redshift cluster|
| action | "block_redshift_public_access" |


## Remediation Execution
Following command need to execute
```sh

ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "aws_region": "xxxx",
  "cluster_identifier": "xxxx",
  "action": "block_redshift_public_access"
}'
```
