from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProductAPIView


# router = DefaultRouter()
# router.register('product',ProductAPIView)
urlpatterns = [
    # path('',include(router.urls)),
    path('product',ProductAPIView.as_view())
]

