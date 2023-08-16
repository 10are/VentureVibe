from ..models import *
from .serializers import *
from rest_framework import viewsets, pagination, permissions
from rest_framework.response import Response

class OrganizationPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CustomOrganizationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_authenticated  
        return True 


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = OrganizationPagination

