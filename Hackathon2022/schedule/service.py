import xlrd
from io import BytesIO, StringIO
import os


class ExcelScheduleService:
    def __init__(self, instance):
        self.schedule_instance = instance

    def post_excel_data(self):
        # with open(self.schedule_instance.excel, 'r'):
        print(self.schedule_instance.excel)
        print(self.schedule_instance)
        book = xlrd.open_workbook_xls('self.schedule_instance.excel')
        print(book)
        # excel_file = self.request_data.get('excel')
        # book = str(excel_file.read())
        # print(book)

        # book = None
        # with BytesIO(excel_file.read()) as file:
        #     print(file)
        #     book = file
        #     print(type(book))
        #     bytes_book = book.read()
        #     print(str(book.decode('utf-8', 'backslashreplace')))
        # with os.popen(f'{excel_file}', 'r') as file:
        #     print(file)
            # print(excel_file)
            # book = xlrd.open_workbook(str(excel_file.read()))
            # book = xlrd.open_workbook_xls(book)

        # print("The number of worksheets is {0}".format(book.nsheets))
        # print("Worksheet name(s): {0}".format(book.sheet_names()))
        # sh = book.sheet_by_index(0)
        # print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
        # print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
        # for rx in range(sh.nrows):
        #     print(sh.row(rx))
