from django.db import models
from django.contrib.auth.models import AbstractUser

from student_group.models import StudentGroup
from .managers import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), blank=False, unique=True)
    edu_group = models.ForeignKey(StudentGroup, on_delete=models.NOT_PROVIDED, blank=True, null=True, default=1)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
