from django.forms import FileField, Form


class MyImportForm(Form):
    import_file = FileField(
        label='File to import'
    )

    def __init__(self, import_formats, *args, **kwargs):
        super().__init__(*args, **kwargs)
