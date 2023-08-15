from rest_framework import serializers
from ..models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

# class OrganizationRatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrganizationRating
#         fields = ['id', 'rating', 'organization', 'user']