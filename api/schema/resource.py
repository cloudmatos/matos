from flask_marshmallow import Schema
from marshmallow.fields import Nested, Dict, List, Str


class AddressSchema(Schema):
    type = Str()
    address = Str()


class AllocatableSchema(Schema):
    class Meta:
        fields = ("attachable-volumes-gce-pd", "hugepages-1Gi",
                  "hugepages-2Mi", "cpu", "ephemeral", "memory", "pods")

    attachable = Str()
    cpu = Str()
    ephemeral = Str()
    hugepages = Str()
    hugepages = Str()
    memory = Str()
    pods = Str()


# Cluster related Schema
class ResourceVpcConfigSchema(Schema):
    clusterSecurityGroupId = Str()
    endpointPrivateAccess = Str()
    endpointPublicAccess = Str()
    publicAccessCidrs = List(Str())
    securityGroupIds = List(Str())
    subnetIds = List(Str())
    vpcId = Str()


class ResourceClusterSelfSchema(Schema):
    name = Str()
    display_name = Str()
    description = Str()
    self_link = Str()
    region = Str()
    endpoint = Str()
    create_time = Str()
    status = Str()
    source_data = Dict()
    arn = Str()
    resource_vpc_config = Nested(ResourceVpcConfigSchema)
    tags = Dict()
    version = Str()
    roleArn = Str()
    platformVersion = Str()
    namespace = List(Dict())
    identity = Str()
    kubernetesNetworkConfig = Str()
    logging = Dict()


# Node related Schema
class NodeConfigSchema(Schema):
    disk_size = Str()
    disk_type = Str()
    machine_type = Str()


class NodeSelfStatusSchema(Schema):
    addresses = List(Nested(AddressSchema))
    allocatable = Nested(AllocatableSchema)
    capacity = Nested(AllocatableSchema)


class ResourceNodeSelfSchema(Schema):
    name = Str()
    display_name = Str()
    cluster_name = Str()
    create_time = Str()
    self_link = Str()
    status = Nested(NodeSelfStatusSchema)
    source_data = Dict()
    instance_id = Str()


class ResourceNodeSelfWrapperSchema(Schema):
    self = Nested(ResourceNodeSelfSchema)


# POD related Schema
class PodSelfStatusSchema(Schema):
    hostIP = Str()
    message = Str()
    nominatedNodeName = Str()
    phase = Str()
    podIP = Str()
    qosClass = Str()
    reason = Str()
    startTime = Str()


class ResourcePodSelfSchema(Schema):
    name = Str()
    display_name = Str()
    cluster_name = Str()
    node_name = Str()
    namespace = Str()
    create_time = Str()
    status = Nested(PodSelfStatusSchema)
    source_data = Dict()


class ResourcePodSelfWrapperSchema(Schema):
    self = Nested(ResourcePodSelfSchema)


# Service related Schema
class ServiceSelfStatusSchema(Schema):
    loadBalancer = Dict()


class ResourceServiceSelfSchema(Schema):
    name = Str()
    cluster_name = Str()
    namespace = Str()
    create_time = Str()
    status = Nested(ServiceSelfStatusSchema)
    source_data = Dict()


class ResourceServiceSelfWrapperSchema(Schema):
    self = Nested(ResourceServiceSelfSchema)


class ResourceClusterSchema(Schema):
    class Meta:
        fields = ("self", "node", "pod", "service", "deployment")

    self = Nested(ResourceClusterSelfSchema)
    node = List(Nested(ResourceNodeSelfWrapperSchema))
    pod = List(Nested(ResourcePodSelfWrapperSchema))
    service = List(Nested(ResourceServiceSelfWrapperSchema))
    deployment = List(Dict())


class ResourceInstanceSelfSchema(Schema):
    id = Str()
    display_name = Str()
    self_link = Str()
    create_time = Str()
    status = Str()
    instance_id = Str()
    instance_type = Str()
    zone = Str()
    source_data = Dict()
    network_interfaces = List(Dict())
    tags = List(Dict())
    subnet_id = Str()
    memory = Dict()
    image_id = Str()
    launch_time = Str()
    cpu_option = Dict()
    block_device_mappings = Dict()


class ResourceInstanceSchema(Schema):
    class Meta:
        fields = ("self",)

    self = Nested(ResourceInstanceSelfSchema)


class ResourceSchema(Schema):
    class Meta:
        fields = [
            'account',
            'cluster',
            'instance',
            'storage',
            'sql',
            'serviceAccount',
            'network',
            'iam',
            'disk',
            'snapshot',
            'log_monitor',
            'kms',
            'policy',
            'no_sql',
            'eip',
            'apphosting',
            'lb',
            'analyzer',
            'filesystem',
            'user_groups',
            'sagemaker',
            'config_service',
            'elasticsearch',
            'guardduty',
            'functions',
            'redshift',
            's3control',
            'dax',
            'opensearch',
            'cloudfront',
            'apigateway',
            'rest_api',
            'sqs',
            'ssm',
            'sns',
            'docdb',
            'logs_metrics',
            'codebuild',
            'glue',
            'acm',
            'securityhub',
            'emr',
            'autoscaling',
            'cloudformation',
            'ecs',
            'ecr',
            'kinesis',
            'elasticache'
        ]

    cluster = List(Nested(ResourceClusterSchema), required=True)
    instance = List(Nested(ResourceInstanceSchema), required=True)
    storage = List(Dict())
    sql = List(Dict())
    serviceAccount = List(Dict())
    network = List(Dict())
    iam = List(Dict())
    disk = List(Dict())
    snapshot = List(Dict())
    kms = List(Dict())
    policy = List(Dict())
    eip = List(Dict())
    log_monitor = List(Dict())
    no_sql = List(Dict())
    apphosting = List(Dict())
    lb = List(Dict())
    analyzer = List(Dict())
    filesystem = List(Dict())
    user_groups = List(Dict())
    functions = List(Dict())
    sagemaker = List(Dict())
    config_service = List(Dict())
    elasticsearch = List(Dict())
    guardduty = List(Dict())
    redshift = List(Dict())
    s3control = List(Dict())
    dax = List(Dict())
    opensearch = List(Dict())
    cloudfront = List(Dict())
    apigateway = List(Dict())
    rest_api = List(Dict())
    sqs = List(Dict())
    ssm = List(Dict())
    sns = List(Dict())
    docdb = List(Dict())
    logs_metrics = List(Dict())
    codebuild = List(Dict())
    glue = List(Dict())
    acm = List(Dict())
    securityhub = List(Dict())
    emr = List(Dict())
    autoscaling = List(Dict())
    cloudformation = List(Dict())
    ecs = List(Dict())
    ecr = List(Dict())
    account = List(Dict())
    kinesis = List(Dict())
    elasticache = List(Dict())
