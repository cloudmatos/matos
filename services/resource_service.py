from providers.factory import ProviderFactory
from utils.reformer import reform_resources


class ResourceService:
    provider = 'gcp'

    def __init__(self, provider):
        self.provider = provider

    def get_resource(self, remove_instance=True):
        """_summary_

        Args:
            remove_instance (bool, optional): remove instance option. Defaults to True.

        Returns:
            Tuple: resource meta data
        """
        pretty_resources = {}
        resources = ProviderFactory(self.provider).find_resources()
        for resource_type, _ in resources.items():
            resource = resources.get(resource_type, {})
            if self.provider == 'gcp':
                pretty_resources = {**pretty_resources, **(reform_resources(self.provider, resource))}
            else:
                if resource_type not in pretty_resources:
                    pretty_resources[resource_type] = []
                for item in resource:
                    reformatted_resource = reform_resources(self.provider, item)
                    pretty_resources[resource_type].extend([reformatted_resource[resource_type]]
                                                           if resource_type in reformatted_resource else [])

        cluster_node_name_list = []
        if remove_instance:
            for cluster in pretty_resources.get('cluster', []):
                cluster_node_name_list.extend(
                    [node['self']['name' if self.provider == 'gcp' else 'instance_id'] for node in cluster.get('node', [])])
            if 'instance' in pretty_resources:
                pretty_resources['instance'] = [rsc for rsc in pretty_resources['instance'] if
                                                rsc['self'].get('display_name', '') not in cluster_node_name_list]

        return pretty_resources, cluster_node_name_list
