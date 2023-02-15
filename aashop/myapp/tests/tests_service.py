import os
from django.test import TestCase

from myapp.services import calc_discont

os.environ['DJANGO_SETTINGS_MODULE'] = 'aashop.settings'


class ServiceTestCase(TestCase):
    def test_calc_discont(self):
        result1 = calc_discont(1_000)
        self.assertEqual(900, result1)
        result2 = calc_discont(0)
        self.assertEqual(0, result2)
        result3 = calc_discont(25.25)
        self.assertEqual(22.73, result3)