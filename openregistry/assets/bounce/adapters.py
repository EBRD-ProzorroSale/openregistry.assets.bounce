# -*- coding: utf-8 -*-
from openregistry.assets.core.adapters import AssetConfigurator, AssetManagerAdapter
from openregistry.assets.core.constants import STATUS_CHANGES


class BounceAssetConfigurator(AssetConfigurator):
    """ BelowThreshold Tender configuration adapter """

    name = "Bounce Asset configurator"
    available_statuses = STATUS_CHANGES


class BounceAssetManagerAdapter(AssetManagerAdapter):
    name = "Asset Manager for bounce asset"
    context = None
    create_validation = []

    def __init__(self, context):
        self.context = context

    def create_asset(self, request):
        self._validate(request, self.create_validation)
