from django.db.models import (
    Model,
    CharField,
    TextField,
    ImageField,
    DateField
)
from django.utils import timezone


class News(Model):
    title = CharField(max_length=80)
    short_desc = CharField(max_length=150)
    description = TextField(max_length=800)
    img = ImageField(upload_to='news_images/', blank=True, null=True)
    date_posted = DateField(default=timezone.localdate, blank=True)
    hashtag = CharField(max_length=40, default='')

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
