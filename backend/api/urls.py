# backend/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NodeViewSet, EdgeViewSet

router = DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'edges', EdgeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
