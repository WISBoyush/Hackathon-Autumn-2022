from django.contrib.admin import register, ModelAdmin
from .models import News


@register(News)
class AdminNews(ModelAdmin):
    list_display = ('__str__', 'title', 'short_desc', 'description', 'date_posted')
