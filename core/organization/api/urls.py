from rest_framework import routers
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

router = routers.DefaultRouter()


router.register(r'organization', OrganizationViewSet)
router.register(r'organizationrating', OrganizationRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)