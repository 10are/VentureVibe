from django.test import TestCase
from ..models import Organization

class OrganizationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(name='Test Organization', business_type='sme', country='TR')

    def test_name_label(self):
        organization = Organization.objects.get(id=1)
        field_label = organization._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_business_type_choices(self):
        organization = Organization.objects.get(id=1)
        business_type = organization.get_business_type_display()
        self.assertEqual(business_type, 'KOBİ')

