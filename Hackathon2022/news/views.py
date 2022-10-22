from rest_framework.viewsets import ModelViewSet
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.all()
