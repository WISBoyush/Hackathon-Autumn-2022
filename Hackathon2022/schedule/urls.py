from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ScheduleViewSet

router = SimpleRouter()
router.register('', ScheduleViewSet, basename='schedule')

urlpatterns = [
    path('', include(router.urls)),
]
