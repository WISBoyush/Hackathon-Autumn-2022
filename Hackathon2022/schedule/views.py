from rest_framework.viewsets import ModelViewSet
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleViewSet(ModelViewSet):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return self.model.objects.all()
