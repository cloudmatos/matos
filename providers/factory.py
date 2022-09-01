from .config import PROVIDER_REGISTER


class ProviderFactory:

    def __init__(self,
                 provider: str,
                 **kwargs,
                 ) -> None:
        """
        Contructor method
        """
        self.provider = provider
        self.kwargs = kwargs

        if provider not in PROVIDER_REGISTER:
            raise NotImplementedError("Provider not implemented yet")

        self.manager = PROVIDER_REGISTER[provider](
            **kwargs,
        )

    def find_resources(self, **kwargs):
        """
        find cloud resources
        """

        assets = self.manager.get_assets(**kwargs)
        resources = self.manager.get_resource_inventories(assets)
        return resources
