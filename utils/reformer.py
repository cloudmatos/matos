# pylint: disable=C0302, R1718, R1710, R1724
from itertools import groupby


def aws_cluster(resource, provider):
    """
    aws cluster info
    """

    cluster = selfish({
        "display_name": from_dict(resource, "name"),
        "name": from_dict(resource, "name"),
        "arn": from_dict(resource, "arn"),
        "endpoint": from_dict(resource, 'endpoint'),
        "resources_vpc_config": from_dict(resource, "resourcesVpcConfig"),
        "created_time": from_dict(resource, 'createdAt'),
        "status": from_dict(resource, "status"),
        "tags": from_dict(resource, "tags"),
        "version": from_dict(resource, "version"),
        "roleArn": from_dict(resource, "roleArn"),
        "platformVersion": from_dict(resource, "platformVersion"),
        "namespace": from_dict(resource, "namespace"),
        "identity": from_dict(resource, "identity"),
        "kubernetesNetworkConfig": from_dict(resource, "kubernetesNetworkConfig"),
        "logging": from_dict(resource, "logging"),
        "region": from_dict(resource, "zone"),
        "source_data": resource
    })

    add_child(aws_cluster_pod, "pod", "pod", resource, cluster, provider)
    add_child(aws_cluster_service, "service", "service", resource, cluster, provider)
    add_child(aws_cluster_node, "node", "node", resource, cluster, provider)

    return cluster


def aws_cluster_pod(resource):
    """
    aws cluster pod
    """

    return selfish({
        'name': resource['name'],
        'namespace': resource['namespace'],
        "source_data": resource
    })


def aws_cluster_node(resource):
    """
    aws cluster node
    """

    return selfish({
        'name': resource['name'],
        'instance_id': resource['instance_id'],
        "source_data": resource
    })


def aws_cluster_service(resource):
    """
    aws cluster service
    """

    return selfish({
        'name': resource['name'],
        'namespace': resource['namespace'],
        "source_data": resource
    })


def aws_glue(resource):
    """AWS clue mapper"""
    glue = selfish({
        "name": "glue",
        "source_data": resource
    })

    return glue


def aws_ecs(resource, provider):
    """AWS ecs mapper"""
    ecs = selfish({
        "name": "ecs",
        "source_data": resource
    })

    return ecs

def aws_ecr(resource, provider):
    """AWS ecs mapper"""
    ecr = selfish({
        "name": "ecr",
        "source_data": resource
    })

    return ecr


def aws_account(resource,provider):
    """AWS account service"""
    account = selfish({
        "name": "account",
        "source_data": resource
    })

    return account


def aws_glue_job(resource):
    """
    aws glue job mapper
    """
    return selfish({
        'name': resource['Name'],
        "source_data": resource
    })


def aws_glue_endpoint(resource):
    """
    aws glue endpoint mapper
    """
    return selfish({
        'name': resource['EndpointName'],
        "source_data": resource
    })


def aws_glue_data_catalogue_encryption_settings(resource):
    """
    aws glue data catalogue mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_glue_crawlers(resource):
    """
    aws glue crawler mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_glue_data_catalogue_resource_policy(resource):
    """
    aws glue data catalogue resource
    """
    return selfish({
        "source_data": resource
    })


def aws_glue_connections(resource):
    """
    aws glue connections mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_instance(resource, provider):
    """
    aws instance mapper
    """

    return selfish({
        "instance_id": from_dict(resource, "InstanceId"),
        "display_name": from_dict(resource, "InstanceId"),
        "instance_type": from_dict(resource, "InstanceType"),
        "region": from_dict(resource, "Placement", "AvailabilityZone"),
        "network_interfaces": from_dict(resource, "NetworkInterfaces"),
        "tags": from_dict(resource, "Tags"),
        "subnet_id": from_dict(resource, "SubnetId"),
        "memory": from_dict(resource, "InstanceMemory"),
        "image_id": from_dict(resource, "ImageId"),
        "launch_time": from_dict(resource, "LaunchTime"),
        "cpu_option": from_dict(resource, "CpuOptions"),
        "block_device_mappings": from_dict(resource, "BlockDeviceMappings"),
        "source_data": resource
    })


def aws_sagemaker(resource, provider):
    """
    Mapper for AWS Sagemaker service.

    Parameters:
    - resource: AWS Sagemaker resource to map
    - provider: provider. AWS/GCP/Azure

    """

    return selfish({
        "notebook_instance_arn": from_dict(resource, "NotebookInstanceArn"),
        "notebook_instance_name": from_dict(resource, "NotebookInstanceName"),
        "source_data": resource
    })


def aws_config_service(resource, provider):
    """
    Mapper for AWS config service.

    Parameters:
    - resource: AWS config resource to map
    - provider: provider. AWS/GCP/Azure

    """

    return selfish({
        "source_data": resource
    })


def aws_elasticsearch(resource, provider):
    """
    Mapper for AWS elasticsearch.

    Parameters:
    - resource: AWS config resource to map
    - provider: provider. AWS/GCP/Azure

    """

    return selfish({
        "source_data": resource
    })


def aws_guardduty(resource, provider):
    """
    Mapper for AWS Guard Duty.

    Parameters:
    - resource: AWS guard duty resource to map
    - provider: provider. AWS/GCP/Azure

    """
    return selfish({
        "source_data": resource
    })


def aws_s3control(resource, provider):
    """
    Mapper for AWS S3Control.

    Parameters:
    - resource: AWS s3control resource to map
    - provider: provider. AWS/GCP/Azure

    """
    return selfish({
        "source_data": resource
    })


def aws_dax(resource, provider):
    """
    Mapper for AWS Dax.

    Parameters:
    - resource: AWS dax resource to map
    - provider: provider. AWS/GCP/Azure

    """
    return selfish({
        "source_data": resource
    })


def aws_network(resource, provider):
    """
    aws network mapper
    """
    return selfish({
        "name": from_dict(resource, "id"),
        "description": from_dict(resource, "description"),
        "status": from_dict(resource, "state"),
        "source_data": resource
    })


def aws_storage(resource, provider):
    """
    aws storage mapper
    """
    return selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource
    })


def aws_sql(resource, provider):
    """
    aws sql mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_cloudtrail(resource, provider):
    """
    aws cloudtrail mapper
    """
    return selfish({
        "name": from_dict(resource, "Name"),
        "source_data": resource
    })


def aws_kms(resource, provider):
    """
    aws kms mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_policy(resource, provider):
    """
    aws policy mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_sa(resource, provider):
    """
    aws sa resource mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_disk(resource, provider):
    """
    aws disk mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_snapshot(resource, provider):
    """
    aws snapshot mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_dynamodb(resource, provider):
    """
    aws dynamodb mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_elasticbeanstalk(resource, provider):
    """
    aws elastic bean stalk mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_elb(resource, provider):
    """
    aws elb mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_analyzer(resource, provider):
    """
    aws analyzer mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_iam(resource, provider):
    """
    aws iam mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_user_groups(resource, provider):
    """
    aws user groups mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_functions(resource, provider):
    """
    aws functiosn mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_redshift(resource, provider):
    """
    aws redshift mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_apigateway(resource, provider):
    """
    aws apigateway mapper
    """
    return selfish({
        "name": from_dict(resource, "Name"),
        "region": from_dict(resource, "ApiEndpoint").split('.')[2],
        "source_data": resource
    })


def aws_rest_api(resource, provider):
    """
    aws rest api mapper
    """
    return selfish({
        "name": from_dict(resource, "Name"),
        "region": from_dict(resource, "region"),
        "source_data": resource
    })


def aws_sqs(resource, provider):
    """
    aws sqs mapper
    """
    return selfish({
        "name": from_dict(resource, "QueueArn").split(':')[-1],
        "region": from_dict(resource, "QueueArn").split(':')[3],
        "source_data": resource
    })


def aws_opensearch(resource, provider):
    """
    aws opensearch mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_cloudfront(resource, provider):
    """
    aws cloudfront mapper
    """
    return selfish({
        "name": from_dict(resource, "Id"),
        "source_data": resource
    })


def aws_ssm(resource, provider):
    """
    aws ssm mapper
    """
    return selfish({
        "name": from_dict(resource, "Name"),
        "region": "global",
        "source_data": resource
    })


def aws_sns(resource, provider):
    """
    aws sns mapper
    """
    resource['Name'] = from_dict(resource, "TopicArn").split(':')[-1]
    return selfish({
        "name": from_dict(resource, "TopicArn").split(':')[-1],
        "region": from_dict(resource, "TopicArn").split(':')[3],
        "source_data": resource
    })


def aws_docdb(resource, provider):
    """
    aws docdb mapper
    """
    return selfish({
        "name": from_dict(resource, "DBClusterArn").split(':')[-1],
        "region": from_dict(resource, "DBClusterArn").split(':')[3],
        "source_data": resource
    })


def aws_logs_metrics(resource, provider):
    """
    aws logs metrics mapper
    """
    return selfish({
        "name": from_dict(resource, "logGroupName"),
        "region": from_dict(resource, "arn").split(':')[3],
        "source_data": resource
    })


def aws_codebuild(resource, provider):
    """
    aws codebuild mapper
    """
    return selfish({
        "name": from_dict(resource, "name"),
        "region": from_dict(resource, "arn").split(':')[3],
        "source_data": resource
    })


def aws_filesystem(resource, provider):
    """
    aws filesystem mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_acm(resource, provider):
    """
    aws acm mapper
    """
    resource['Name'] = from_dict(resource, "CertificateArn").split(':')[-1]
    return selfish({
        "name": from_dict(resource, "CertificateArn").split(':')[-1],
        "region": from_dict(resource, "CertificateArn").split(':')[3],
        "source_data": resource
    })


def aws_securityhub(resource, provider):
    """
    aws security hub mapper
    """
    return selfish({
        "name": from_dict(resource, "HubArn").split(':')[-1],
        "region": from_dict(resource, "HubArn").split(':')[3],
        "source_data": resource
    })


def aws_emr(resource, provider):
    """
    aws emr mapper
    """
    cluster = selfish({
        "name": "emr",
        "source_data": resource
    })

    return cluster


def aws_emr_cluster(resource):
    """
    aws emr cluster mapper
    """
    return selfish({
        'name': resource['Id'],
        'region': resource['ClusterArn'].split(":")[3],
        "source_data": resource
    })


def aws_emr_block_public_access_configuration(resource):
    """
    aws emr block mapper
    """
    return selfish({
        "source_data": resource
    })


def azure_cluster(resource, provider):
    """
    aws cluster mapper
    """
    temp_resource = {**resource}
    del temp_resource['pod']
    del temp_resource['service']
    cluster = selfish({
        "name": from_dict(resource, "name"),
        "source_data": temp_resource
    })

    add_child(azure_cluster_pod, "pod", "pod",
              {**resource, "pod": [{**pod, "cluster_name": from_dict(resource, "name")} for pod in resource['pod']]},
              cluster, provider)
    add_child(azure_cluster_node, "node", "node", {**resource,
                                                   "node": [{"name": node, "cluster_name": from_dict(resource, "name")}
                                                            for node in list(set(
                                                           [from_dict(pod, "spec", "node_name") for pod in
                                                            resource['pod']]))]}, cluster, provider)
    add_child(azure_cluster_service, "service", "service", {**resource, "service": [
        {**service, "cluster_name": from_dict(resource, "name")} for service in resource['service']]}, cluster,
              provider)

    return cluster


def aws_autoscaling(resource, provider):
    """
    aws autoscaling mapper
    """
    return selfish({
        "name": resource['AutoScalingGroupName'],
        "region": resource['AutoScalingGroupARN'].split(':')[3],
        "source_data": resource
    })


def aws_cloudformation(resource, provider):
    """
    aws cloudformation mapper
    """
    return selfish({
        "source_data": resource
    })


def aws_kinesis_stream(resource, provider):
    """
    aws kinesis stream mapper
    """
    return selfish({
        "source_data": resource
    })


def azure_cluster_pod(resource):
    """
    azure cluster mapper
    """
    return selfish({
        "name": from_dict(resource, "metadata", 'name'),
        "display_name": from_dict(resource, "metadata", 'name'),
        "namespace": from_dict(resource, "metadata", 'namespace'),
        "cluster_name": from_dict(resource, "cluster_name"),
        "node_name": from_dict(resource, "spec", 'node_name'),
        "source_data": resource
    })


def azure_cluster_service(resource):
    """azure cluster service mapper"""
    return selfish({
        "name": from_dict(resource, "metadata", 'name'),
        "display_name": from_dict(resource, "metadata", 'name'),
        "namespace": from_dict(resource, "metadata", 'namespace'),
        "cluster_name": from_dict(resource, "cluster_name"),
        "source_data": resource
    })


def azure_cluster_node(resource):
    """azure cluster node mapper"""
    return selfish({
        "instance_id": from_dict(resource, 'name'),
        "name": from_dict(resource, 'name'),
        "display_name": from_dict(resource, 'name'),
        "cluster_name": from_dict(resource, "cluster_name"),
        "source_data": resource
    })


def azure_instance(resource, provider):
    """
    azure instance mapper
    """

    instance = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource
    })

    return instance


def azure_network(resource, provider):
    """
    azure network mapper
    """

    network = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource
    })

    return network


def azure_storage(resource, provider):
    """
    azure storage mapper
    """

    storage = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource
    })

    return storage


def azure_sql(resource, provider):
    """
    azure sql mapper
    """

    sql = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource
    })

    return sql


def azure_monitor(resource, provider):
    """
    azure monitor mapper
    """

    monitor = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource,
        "region": from_dict(resource, "location")
    })

    return monitor


def azure_postgreSQL(resource, provider):
    """
    azure postgreSQL mapper
    """

    postgreSQL = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource,
        "region": from_dict(resource, "servers", "location")
    })

    return postgreSQL


def azure_key_vault(resource, provider):
    """
    awzure key vault mapper
    """

    key_vault = selfish({
        "name": from_dict(resource, "name"),
        "source_data": resource,
        "region": from_dict(resource, "location")
    })

    return key_vault


def gcp_cluster(resource, provider):
    """
    Add properties as required from the API result.
    """

    cluster_details = resource['cluster']
    clusters = []

    if isinstance(cluster_details, list):
        for cluster_item in cluster_details:
            cluster = selfish({
                "name": from_dict(cluster_item, "resource", "data", "name"),
                "display_name": from_dict(cluster_item, "resource", "data", "name"),
                "description": from_dict(cluster_item, "resource", "data", "description"),
                "self_link": from_dict(cluster_item, "resource", "data", "selfLink"),
                "region": from_dict(cluster_item, "resource", "data", "zone"),
                "endpoint": from_dict(cluster_item, "resource", "data", "endpoint"),
                "create_time": from_dict(cluster_item, "resource", "data", "createTime"),
                "status": from_dict(cluster_item, 'resource', 'data', 'status'),
                "source_data": from_dict(cluster_item, 'resource', 'data'),
            })

            add_child(gcp_cluster_pod, "pods", "pod", resource, cluster, provider)
            add_child(gcp_cluster_service, "services", "service", resource, cluster, provider)
            add_child(gcp_cluster_node, "nodes", "node", resource, cluster, provider)
            add_child(gcp_cluster_deployment, "deployments", "deployment", resource, cluster, provider)

            clusters.append(cluster)

    return clusters


def gcp_cluster_node(resource):
    """
    gcp cluster node mapper
    """

    return selfish({
        "name": from_dict(resource, "resource", "data", "metadata", "name"),
        "display_name": from_dict(resource, "resource", "data", "metadata", "name"),
        "self_link": from_dict(resource, "resource", "data", "metadata", "selfLink"),
        "cluster_name": from_dict(resource, "cluster_name"),
        "create_time": from_dict(resource, "resource", "data", "metadata", "creationTimestamp"),
        "status": from_dict(resource, "resource", "data", "status"),
        "source_data": from_dict(resource, "resource", "data")
    })


def gcp_cluster_pod(resource):
    """
    gcp cluster pod mapper
    """

    return selfish({
        "name": from_dict(resource, "resource", "data", "metadata", "name"),
        "display_name": from_dict(resource, "resource", "data", "metadata", "name"),
        "cluster_name": from_dict(resource, "cluster_name"),
        "node_name": from_dict(resource, "resource", "data", "spec", "nodeName"),
        "namespace": from_dict(resource, "resource", "data", "metadata", "namespace"),
        "create_time": from_dict(resource, "resource", "data", "metadata", "creationTimestamp"),
        "status": from_dict(resource, "resource", "data", "status"),
        "source_data": from_dict(resource, "resource", "data"),
    })


def gcp_cluster_service(resource):
    """
    gcp cluster service mapper
    """

    return selfish({
        "name": from_dict(resource, "resource", "data", "metadata", "name"),
        "cluster_name": from_dict(resource, "cluster_name"),
        "namespace": from_dict(resource, "resource", "data", "metadata", "namespace"),
        "create_time": from_dict(resource, "resource", "data", "metadata", "creationTimestamp"),
        "status": from_dict(resource, "resource", "data", "status"),
        "source_data": from_dict(resource, "resource", "data")
    })


def gcp_cluster_deployment(resource):
    """
    gcp cluster deployment mapper
    """

    return selfish({
        # "name": from_dict(resource, "resource", "data", "metadata", "name"),
        # "cluster_name": from_dict(resource, "cluster_name"),
        # "namespace": from_dict(resource, "resource", "data", "metadata", "namespace"),
        # "create_time": from_dict(resource, "resource", "data", "metadata", "creationTimestamp"),
        # "status": from_dict(resource, "resource", "data", "status"),
        "source_data": from_dict(resource, "resource", "data")
    })


def gcp_instance(resource, provider):
    """
    gcp instance mapper
    """

    instance_details = resource['instance']

    instances = []
    if isinstance(instance_details, list):
        for instance_item in instance_details:
            instances.append(selfish({
                "instance_id": from_dict(instance_item, "resource", "data", "id"),
                "name": from_dict(instance_item, "resource", "data", "name"),
                "display_name": from_dict(instance_item, "resource", "data", "name"),
                "self_link": from_dict(instance_item, "resource", "data", "selfLink"),
                "create_time": from_dict(instance_item, "resource", "data", "creationTimestamp"),
                "status": from_dict(instance_item, "resource", "data", "status"),
                "source_data": from_dict(instance_item, "resource", "data"),
                "zone": from_dict(instance_item, "resource", "data", "zone")
            }))
    return instances


def gcp_network(resource, provider):
    """Gcp network mapper"""
    network_details = resource['network']
    networks = []

    if isinstance(network_details, list):
        for network_item in network_details:
            network = selfish({
                "name": from_dict(network_item, "resource", "data", "name"),
                "display_name": from_dict(network_item, "resource", "data", "name"),
                "self_link": from_dict(network_item, "resource", "data", "selfLink"),
                "source_data": from_dict(network_item, 'resource', 'data'),
                # "source_data": network_item,
            })

            add_child(gcp_network_subnetwork, "subnetworks", "subnetwork", resource, network, provider)
            add_child(gcp_network_firewall, "firewalls", "firewall", resource, network, provider)
            add_child(gcp_network_route, "routes", "route", resource, network, provider)

            networks.append(network)

    return networks


def gcp_network_subnetwork(resource):
    """GCP network subnetwork mapper"""
    return selfish({
        "name": from_dict(resource, "resource", "data", "name"),
        "display_name": from_dict(resource, "resource", "data", "name"),
        "network": from_dict(resource, "network_name"),
        "region": from_dict(resource, "resource", "data", "region"),
        "source_data": from_dict(resource, "resource", "data"),
    })


def gcp_network_firewall(resource):
    """gcp network firewall mapper"""
    return selfish({
        "name": from_dict(resource, "resource", "data", "name"),
        "display_name": from_dict(resource, "resource", "data", "name"),
        "network": from_dict(resource, "network_name"),
        "source_data": from_dict(resource, "resource", "data"),
    })


def gcp_network_route(resource):
    """gcp network route mapper"""
    return selfish({
        "name": from_dict(resource, "resource", "data", "name"),
        "display_name": from_dict(resource, "resource", "data", "name"),
        "network": from_dict(resource, "network_name"),
        "source_data": from_dict(resource, "resource", "data"),
    })


def gcp_storage(resource, provider):
    """gcp storage mapper"""
    storage_details = resource['storages']
    storages = []

    if isinstance(storage_details, list):
        for storage_item in storage_details:
            storage = selfish({
                "name": from_dict(storage_item, "resource", "data", "name").split('/')[-1],
                "display_name": from_dict(storage_item, "resource", "data", "name").split('/')[-1],
                "asset_type": "bucket",
                "source_data": from_dict(storage_item, 'resource', 'data'),
                "iam_policy": from_dict(storage_item, 'iamPolicy'),
                "ancestors": from_dict(storage_item, 'ancestors')
            })

            # add_child(gcp_network_subnetwork, "subnetworks", "subnetwork", resource, storage, provider)
            # add_child(gcp_network_firewall, "firewalls", "firewall", resource, storage, provider)
            # add_child(gcp_network_route, "routes", "route", resource, storage, provider)

            storages.append(storage)

    return storages


def gcp_service_account(resource, provider):
    """gcp service account"""
    service_account_details = resource['serviceAccount']
    service_account_list = []

    if isinstance(service_account_details, list):
        for service_account_item in service_account_details:
            service_account = selfish({
                "name": from_dict(service_account_item, "resource", "data", "name"),
                "resource": from_dict(service_account_item, 'resource', 'data'),
                "iam_policy": from_dict(service_account_item, 'iamPolicy'),
                "ancestors": from_dict(service_account_item, 'ancestors'),
                "source_data": {
                    **service_account_item,
                    "serviceAccountKey": [{
                        "key": akey['name'].split('/')[-1],
                        "name": akey['name'],
                        **akey['resource']['data']
                    } for akey in resource['serviceAccountKey'] if
                        akey['serviceAccount_name'] ==
                        from_dict(service_account_item, 'resource', 'data')['uniqueId']]
                }
            })

            service_account_list.append(service_account)

    return service_account_list


def gcp_service_account_key(resource):
    """gcp service account key mapper"""
    return selfish({**from_dict(resource, "resource", "data")})


def gcp_sql(resource, provider):
    """gcp sql mapper"""
    sql_details = resource['sql']
    sqls = []

    if isinstance(sql_details, list):
        for sql_item in sql_details:
            sql = selfish({
                "name": from_dict(sql_item, "resource", "data", "name"),
                "display_name": from_dict(sql_item, "resource", "data", "name"),
                "source_data": from_dict(sql_item, 'resource', 'data'),
            })

            sqls.append(sql)

    return sqls


def gcp_project(resource, provider):
    """gcp project mapper"""
    project_details = resource['iam']
    project_list = []

    if isinstance(project_details, list):
        for service_account_item in project_details:
            service_account = selfish({
                "name": from_dict(service_account_item, "resource", "data", "name"),
                # "resource": from_dict(service_account_item, 'resource', 'data'),
                "iam_policy": from_dict(service_account_item, 'iamPolicy'),
                "source_data": service_account_item
            })

            project_list.append(service_account)

    return project_list


def gcp_disk(resource, provider):
    """gcp disk mapper"""
    disk_details = resource['disk']
    disk_list = []

    if isinstance(disk_details, list):
        for disk_item in disk_details:
            service_account = selfish({
                "name": from_dict(disk_item, "resource", "data", "name"),
                "source_data": disk_item
            })

            disk_list.append(service_account)

    return disk_list


def gcp_snapshot(resource, provider):
    """gcp snapshot mapper"""
    snapshot_details = resource['snapshot']
    snapshot_list = []

    if isinstance(snapshot_details, list):
        for snapshot_item in snapshot_details:
            service_account = selfish({
                "name": from_dict(snapshot_item, "resource", "data", "name"),
                "source_data": snapshot_item
            })

            snapshot_list.append(service_account)

    return snapshot_list


cloud_resource_mappers = {
    'aws': {
        'cluster': aws_cluster,
        'cluster_pod': None,
        'cluster_service': None,
        'cluster_node': None,
        'instance': aws_instance,
        'storage': aws_storage,
        'network': aws_network,
        'sql': aws_sql,
        'log_monitor': aws_cloudtrail,
        'kms': aws_kms,
        'policy': aws_policy,
        'serviceAccount': aws_sa,
        'no_sql': aws_dynamodb,
        'disk': aws_disk,
        'snapshot': aws_snapshot,
        'eip': aws_snapshot,
        'apphosting': aws_elasticbeanstalk,
        'lb': aws_elb,
        'iam': aws_elb,
        'analyzer': aws_analyzer,
        'filesystem': aws_filesystem,
        'user_groups': aws_user_groups,
        'sagemaker': aws_sagemaker,
        'config_service': aws_config_service,
        'elasticsearch': aws_elasticsearch,
        'guardduty': aws_guardduty,
        's3control': aws_s3control,
        'dax': aws_dax,
        'functions': aws_functions,
        'redshift': aws_redshift,
        'opensearch': aws_opensearch,
        'cloudfront': aws_cloudfront,
        'apigateway': aws_apigateway,
        'rest_api': aws_rest_api,
        'sqs': aws_sqs,
        'ssm': aws_ssm,
        'sns': aws_sns,
        'docdb': aws_docdb,
        'logs_metrics': aws_logs_metrics,
        'codebuild': aws_codebuild,
        'glue': aws_glue,
        'ecs': aws_ecs,
        'ecr': aws_ecr,
        'account': aws_account,
        'acm': aws_acm,
        'securityhub': aws_securityhub,
        'emr': aws_emr,
        'autoscaling': aws_autoscaling,
        'cloudformation': aws_cloudformation,
        'kinesis': aws_kinesis_stream

    },
    'azure': {
        'cluster': azure_cluster,
        'instance': azure_instance,
        'network': azure_network,
        'storage': azure_storage,
        'sql': azure_sql,
        'log_monitor': azure_monitor,
        'postgreSQL': azure_postgreSQL,
        'key_vault': azure_key_vault,

    },
    'gcp': {
        'cluster': gcp_cluster,
        'cluster_pod': None,
        'cluster_service': None,
        'cluster_node': None,
        'instance': gcp_instance,
        'network': gcp_network,
        "storage": gcp_storage,
        "serviceAccount": gcp_service_account,
        'sql': gcp_sql,
        'iam': gcp_project,
        'disk': gcp_disk,
        'snapshot': gcp_snapshot
    }
}


def from_dict(data, *paths, raise_error=False):
    """
    convert value from dict
    """

    last_value = data

    for current_path in paths:

        if isinstance(last_value, (list, tuple)):

            if not isinstance(current_path, int):
                if raise_error:
                    raise KeyError(f"{current_path} should be a integer,"
                                   " target value is a sequence")
                return

            last_value = last_value[current_path]
            continue

        elif isinstance(last_value, dict):

            if current_path not in last_value:
                if raise_error:
                    raise KeyError(f"{current_path} is not present in target")
                return

            last_value = last_value[current_path]
            continue

        if raise_error:
            raise KeyError(f"{type(last_value)} is not "
                           f"accessible with key {current_path}")
        return

    return last_value


def selfish(data):
    """mapper data"""
    return {
        "self": data
    }


def check_support(provider, res_type):
    """check provider support"""
    if provider not in cloud_resource_mappers:
        raise NotImplementedError(
            f"{provider} cloud provider is not supported yet")

    if res_type not in cloud_resource_mappers[provider]:
        raise NotImplementedError(f"{res_type} resource type is"
                                  f" not yet supported for {provider}")


def add_child(child_mapper,
              source_key,
              target_key,
              source_data,
              target_data,
              provider='gcp'
              ):
    """
    add child mapper
    """

    if source_key not in source_data:
        target_data.update({target_key: []})
        return
    try:
        data = source_data[source_key]

        if not data:
            return

        if isinstance(data, (list, tuple, set)):
            mapped = [child_mapper(s) for s in data if (from_dict(s, "cluster_name") == target_data['self']['name']
                                                        or from_dict(s, 'network_name') == target_data['self']['name']
                                                        or (source_key == 'serviceAccountKey'
                                                            and from_dict(s, "serviceAccount_name") ==
                                                            target_data['self']['resource']['uniqueId']))
                      and provider == 'gcp' or provider != 'gcp']
        else:
            mapped = child_mapper(data) if from_dict(data, "cluster_name") == target_data['self'][
                'name'] and provider == 'gcp' or provider != 'gcp' else None

        target_data.update({target_key: mapped})
    except Exception as ex:
        print("add child error ==== ", ex)
        return


def map_child(child_mapper,
              source_key,
              target_key,
              source_data,
              target_data,
              provider='gcp'
              ):
    """
    map child data
    """
    # map_child(aws_emr_cluster, "Clusters", "Clusters", resource, cluster, provider)
    if source_key not in source_data:
        target_data.update({target_key: []})
        return
    try:
        data = source_data[source_key]

        if not data:
            return

        if isinstance(data, (list, tuple, set)):
            mapped = [child_mapper(s) for s in data if
                      provider == 'gcp' or provider != 'gcp']
        else:
            mapped = child_mapper(data) if provider == 'gcp' or provider != 'gcp' else None

        target_data.update({target_key: mapped})
    except Exception as ex:
        print("add child error ==== ", ex)
        return


def mapper(provider, res_type, resource):
    """
    return mapper object
    """

    res_mapper = cloud_resource_mappers[provider][res_type]

    if isinstance(resource, (list, tuple, set)):
        return [res_mapper(r, provider) for r in resource]

    return res_mapper(resource, provider)


def group_resources(resources):
    """
    group resources
    """

    def key(resource):
        return resource['type']

    resources.sort(key=key)

    return {res_type: list(group)
            for res_type, group in groupby(resources, key=key)}


def reform_resources(provider, resources):
    """
    reform resources
    """

    retdict = {}
    if isinstance(resources, dict):
        res_type = resources.get('type')
        details = resources.get('details')
        if res_type == 'cluster' and provider == 'aws':
            details['zone'] = resources['location']

        if not details:
            return retdict

        try:
            check_support(provider, res_type)
        except NotImplementedError:
            details = {'self': details}
        else:
            details = mapper(provider, res_type, details)

        retdict[res_type] = details

    return retdict
