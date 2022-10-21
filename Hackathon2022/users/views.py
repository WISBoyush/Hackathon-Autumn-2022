from users.models import User
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return User.objects.filter(pk=self.request.user.pk)
        return User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]
