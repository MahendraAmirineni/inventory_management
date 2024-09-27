from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cached_items = cache.get('inventory_items')
        if cached_items is not None:
            return cached_items
        items = super().get_queryset()
        cache.set('inventory_items', items, timeout=60*15)  # Cache for 15 minutes
        return items

    def perform_create(self, serializer):
        logger.info("Creating a new inventory item.")
        serializer.save()

    def perform_update(self, serializer):
        logger.info("Updating inventory item: %s", serializer.instance.name)
        serializer.save()

    def perform_destroy(self, instance):
        logger.info("Deleting inventory item: %s", instance.name)
        instance.delete()
