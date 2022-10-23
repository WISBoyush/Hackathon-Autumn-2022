import pandas as pd
from .models import Schedule
from student_group.models import StudentGroup


class ExcelScheduleService:
    def __init__(self, request_data):
        self.excel_file = request_data

    def post_excel_data(self):
        df = pd.read_excel(self.excel_file, sheet_name='template')
        Schedule.objects.all().delete()
        bulk_create_list = []
        for row_index, row in df.iterrows():
            temp_list = [row_index + 1]
            for index, value in enumerate(row):
                if index == 0:
                    temp_list.append(StudentGroup.objects.get_or_create(group_title=value)[0].pk)
                else:
                    temp_list.append(value)
            bulk_create_list.append(Schedule(*temp_list))
        return Schedule.objects.bulk_create(bulk_create_list)
