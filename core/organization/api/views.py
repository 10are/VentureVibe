from ..models import *
from .serializers import *
from rest_framework import viewsets, pagination
from rest_framework.response import Response

class OrganizationPagination(pagination.PageNumberPagination):
    page_size = 4
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = OrganizationPagination

class OrganizationRatingViewSet(viewsets.ModelViewSet):
    queryset = OrganizationRating.objects.all()
    serializer_class = OrganizationRatingSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        like_count = OrganizationRating.objects.filter(organization=instance.organization, rating='like').count()
        dislike_count = OrganizationRating.objects.filter(organization=instance.organization, rating='dislike').count()
        instance.organization.like_count = like_count
        instance.organization.dislike_count = dislike_count
        instance.organization.save()
