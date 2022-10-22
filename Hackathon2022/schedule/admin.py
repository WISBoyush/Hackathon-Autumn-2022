from django.contrib.admin import ModelAdmin, register
from .models import Schedule


@register(Schedule)
class AdminSchedule(ModelAdmin):
    list_display = ('__str__', 'group_user', 'subject', 'teacher', 'type_of_week',
                    'day_of_week', 'serial_number_of_lesson', 'auditory')
