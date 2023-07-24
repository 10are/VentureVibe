from ..models import *
from .serializers import *
from rest_framework import viewsets, pagination
from rest_framework.response import Response


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = pagination.PageNumberPagination

