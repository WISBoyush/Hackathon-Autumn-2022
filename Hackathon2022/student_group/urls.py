from django.urls import path
from rest_framework.viewsets import ModelViewSet

from .models import StudentGroup
from .serializers import StudentGroupSerializer

urlpatterns = [
    path(
        '',
        ModelViewSet.as_view(
            {'get': 'list', 'post': 'create'},
            queryset=StudentGroup.objects.all(),
            serializer_class=StudentGroupSerializer
        )
    )
]
