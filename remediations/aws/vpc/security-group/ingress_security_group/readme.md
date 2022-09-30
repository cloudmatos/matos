[<img src="https://github.com/cloudmatos/Matos/blob/main/images/matos-logo.png" width="200" height="200">](https://www.cloudmatos.com/)

# Remediation Ensure no security groups allow ingress from 0.0.0.0/0 or ::/0 to port xxx

| # | Port |
|---|---|
| 1 | port 22  |
| 2 | port 3389 |
| 3 | any port |
| 5 | Oracle ports 1521 or 2483 |
| 6 | MySQL port 3306 |
| 7 | Postgres port 5432 |
| 8 | Redis port 6379 |
| 9 | MongoDB ports 27017 and 27018 |
| 10 | Cassandra ports 7199 or 9160 or 8888 |
| 11 | Memcached port 11211 |
| 12 | FTP ports 20 or 21 |
| 13 | Kafka port 9092 |
| 14 | Telnet port 23 |
| 15 | Windows SQL Server ports 1433 or 1434 |


Security groups are stateful and provide filtering of ingress/egress network traffic to AWS resources. We recommend that security groups do not allow unrestricted ingress access to port eg:22, 3306 etc. 

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
| security_groups | security groups info |

## Remediation Execution
Following command need to execute
```sh

ansible-playbook playbook.yml --extra-vars '{
  "aws_secret_key": "XXXXX",
  "aws_access_key": "XXXXX",
  "aws_region": "XXXXX",
  "security_groups":[{
    "GroupId":"sg-xxxxx", 
    "IpPermissions":[{
        "FromPort":"22 or 3306 etc.", 
        "ToPort":"22 or 3306 etc.",
        "IpProtocol":"tcp",
        "Ipv6Ranges":[],
        "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
        }]
    }]
}'
```
