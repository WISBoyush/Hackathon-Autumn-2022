from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    DateTimeField,
    EmailField,
    BooleanField,
    ChoiceField
)
from .models import User

choices = [('student', 'student'), ('tutor', 'tutor'), ('staff', 'staff')]


class UserSerializer(Serializer):  # noqa
    id = IntegerField(read_only=True)
    role = ChoiceField(choices=choices, write_only=True)
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password = CharField()
    is_superuser = BooleanField(read_only=True)
    is_staff = BooleanField(read_only=True)
    is_active = BooleanField(read_only=True)
    date_joined = DateTimeField(read_only=True)
    last_login = DateTimeField(read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            role=validated_data.get('role')
        )
