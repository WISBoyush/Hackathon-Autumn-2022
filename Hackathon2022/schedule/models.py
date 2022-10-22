from django.db.models import CharField, Model, FileField


class Schedule(Model):
    group_user = CharField(max_length=15, default='')
    subject = CharField(max_length=120, null=True)
    teacher = CharField(max_length=120, null=True)
    excel = FileField(upload_to='excels/', default='')

    # even = 'Четная'
    # odd = 'Нечетная'
    # same = 'Еженедельно'
    type_of_week_choices = (
        ('Четная', 'Четная'),
        ('Нечетная', 'Нечетная'),
        ('Еженедельно', 'Еженедельно'),
    )
    type_of_week = CharField(
        max_length=25,
        choices=type_of_week_choices,
        default=type_of_week_choices[0][0],
    )

    # Monday = '1Понедельник'
    # Tuesday = '2Вторник'
    # Wednesday = '3Среда'
    # Thursday = '4Четверг'
    # Friday = '5Пятница'
    # Saturday = '6Суббота'
    day_of_week_choices = (
        ('1Понедельник', 'Понедельник'),
        ('2Вторник', 'Вторник'),
        ('3Среда', 'Среда'),
        ('4Четверг', 'Четверг'),
        ('5Пятница', 'Пятница'),
        ('6Суббота', 'Суббота'),
    )
    day_of_week = CharField(
        max_length=25,
        choices=day_of_week_choices,
        default=day_of_week_choices[0][0],
    )

    # First = '1'
    # Second = '2'
    # Third = '3'
    # Fourth = '4'
    # Fifth = '5'
    # Sixth = '6'
    serial_number_of_lesson_choices = (
        ('1', 'Первая'),
        ('2', 'Вторая'),
        ('3', 'Третья'),
        ('4', 'Четвертая'),
        ('5', 'Пятая'),
        ('6', 'Шестая'),
    )
    serial_number_of_lesson = CharField(
        max_length=1,
        choices=serial_number_of_lesson_choices,
        default=serial_number_of_lesson_choices[0][0],
    )

    auditory = CharField(max_length=10, null=True)

    # def __str__(self):
    #     return self.subject
