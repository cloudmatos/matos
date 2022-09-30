[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation - Ensure there are no EBS Snapshots set as Public

We recommend your EBS snapshots are not publicly accessible. Public AWS EBS snapshot means that data which is backed up in that particular snapshot is accessible to all other AWS accounts. This means the other person can not only access and copy your data but can also create a volume out of it.

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
| snapshot_ids | id's of snapshots |
| disable_public_snapshot | True/False |


## Remediation Execution
Following command need to execute
```sh
ansible-playbook playbook.yml --extra-vars '{
  "aws_access_key": "xxxx",
  "aws_secret_key": "xxxx",
  "region": "xxxx",
  "snapshot_ids":["snap-xxxx"],
  "disable_public_snapshot":True}
}'