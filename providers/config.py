# -*- coding: utf-8 -*-
from matos_aws_provider.provider import Provider as AWSProvider
from matos_azure_provider.provider import Provider as AzureProvider
from matos_gcp_provider.provider import Provider as GCPProvider


PROVIDER_REGISTER = {
    "aws": AWSProvider,
    "gcp": GCPProvider,
    "azure": AzureProvider
}

PROVIDERS = PROVIDER_REGISTER.keys()
