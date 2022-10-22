from rest_framework.serializers import ModelSerializer
from .models import StudentGroup


class StudentGroupSerializer(ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = '__all__'
