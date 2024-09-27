from rest_framework.test import APITestCase
from rest_framework import status
from .models import InventoryItem

class InventoryItemTests(APITestCase):

    def setUp(self):
        self.item = InventoryItem.objects.create(name="Test Item", quantity=10, price=9.99)

    def test_create_item(self):
        response = self.client.post('/api/inventory/', {'name': 'New Item', 'quantity': 5, 'price': 12.99})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        response = self.client.get(f'/api/inventory/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        response = self.client.put(f'/api/inventory/{self.item.id}/', {'name': 'Updated Item', 'quantity': 15, 'price': 19.99})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        response = self.client.delete(f'/api/inventory/{self.item.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
