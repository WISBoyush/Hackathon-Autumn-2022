import django.conf
import pandas
import xlrd
from io import BytesIO, StringIO
import os


class ExcelScheduleService:
    def __init__(self, instance):
        self.schedule_instance = instance

    def post_excel_data(self):
        book = pandas.read_excel(f'{django.conf.settings.MEDIA_ROOT}/{self.schedule_instance.excel}')

