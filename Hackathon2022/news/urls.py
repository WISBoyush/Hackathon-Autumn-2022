from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import NewsViewSet

router = SimpleRouter()
router.register('', NewsViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
