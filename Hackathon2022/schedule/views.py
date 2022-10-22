from rest_framework.viewsets import ModelViewSet
from .models import Schedule
from .serializers import ScheduleSerializer
from .service import ExcelScheduleService

# import os


class ScheduleViewSet(ModelViewSet):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return self.model.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = self.model.objects.all().last()
        service = ExcelScheduleService(instance)
        service.post_excel_data()
