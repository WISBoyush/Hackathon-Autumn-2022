from django.db import models

from users.models import User


class Chat(models.Model):
    answer = models.TextField(max_length=1000)
    from_user = models.ForeignKey(User, on_delete=models.NOT_PROVIDED, blank=True, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.NOT_PROVIDED, blank=True, related_name='to_user')
    question = models.TextField(max_length=1000, blank=True)
    time_to_public = models.DateTimeField(blank=True)
    status = models.CharField(max_length=200,
                              choices=(('AWAITING_ANSWER', 'AWAITING_ANSWER'), ('ANSWERED', 'ANSWERED')),
                              default='AWAITING_ANSWER')
