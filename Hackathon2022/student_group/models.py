from django.db import models


class StudentGroup(models.Model):
    group_title = models.CharField(max_length=50)

