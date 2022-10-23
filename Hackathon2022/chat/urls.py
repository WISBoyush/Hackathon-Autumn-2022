from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ChatViewSet

router = SimpleRouter()
router.register('', ChatViewSet, basename='chat')

urlpatterns = [
    path('', include(router.urls)),
]
