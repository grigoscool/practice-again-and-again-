# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aashop.settings")
# import django
# django.setup()
#
#
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# class ItemTestCase(APITestCase):
#     def test_get(self):
#         url = reverse('item-list')
#         print(url)
#         response = self.client.get(url)
#         print(response)
#         self.assertEqual(status.HTTP_200_OK, response.status_code)