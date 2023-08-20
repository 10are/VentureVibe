from django.test import TestCase
from rest_framework.test import APIRequestFactory
from ..api.views import OrganizationViewSet
from ..models import Organization

class OrganizationViewSetTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(name='Org 1', business_type='sme', country='TR')
        Organization.objects.create(name='Org 2', business_type='large', country='US')

    def test_get_organizations(self):
        factory = APIRequestFactory()
        request = factory.get('/api/organizations/')
        view = OrganizationViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

