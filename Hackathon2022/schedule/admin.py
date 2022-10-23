from django.contrib.admin import ModelAdmin, register
from django.http import HttpResponseRedirect
from import_export.admin import ImportMixin

from .forms import MyImportForm
from .models import Schedule
from .service import ExcelScheduleService


@register(Schedule)
class AdminSchedule(ImportMixin, ModelAdmin):
    list_display = ('group_user', 'subject', 'teacher',
                    'day_of_week', 'serial_number_of_lesson', 'auditory')
    import_form_class = MyImportForm

    def import_action(self, request, *args, **kwargs):
        if request.method == 'GET':
            return super().import_action(request, *args, **kwargs)
        service = ExcelScheduleService(request_data=request.FILES['import_file'])
        service.post_excel_data()
        return HttpResponseRedirect('../')
