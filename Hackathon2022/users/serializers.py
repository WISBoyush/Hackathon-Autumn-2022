from rest_framework.serializers import (
    Serializer,
    IntegerField,
    CharField,
    DateTimeField,
    EmailField,
    BooleanField,
    ChoiceField
)
from users.models import User

choices = [('student', 'student'), ('tutor', 'tutor'), ('staff', 'staff')]


class UserSerializer(Serializer):  # noqa
    id = IntegerField(read_only=True)
    role = ChoiceField(choices=choices, write_only=True)
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password = CharField()
    is_superuser = BooleanField(required=False)
    is_staff = BooleanField(required=False)
    is_active = BooleanField(required=False)
    date_joined = DateTimeField(required=False)
    last_login = DateTimeField(required=False)

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            role=validated_data.get('role')
        )
