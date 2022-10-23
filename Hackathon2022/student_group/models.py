from django.db import models


class StudentGroup(models.Model):
    group_title = models.CharField(max_length=50)

    def __str__(self):
        return self.group_title
