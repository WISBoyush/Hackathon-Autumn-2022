from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer
from .service import ExcelScheduleService
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ScheduleViewSet(ModelViewSet):
    model = Schedule
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        return self.model.objects.all()

    def get_permissions(self):
        # TODO сделать group permissions
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        if 'excel' not in request.data:
            return super().create(request, *args, **kwargs)

        service = ExcelScheduleService(request_data=request.data)
        data = service.post_excel_data()

        return Response(self.serializer_class(data, many=True).data, status=201)
