from django.db.models import CharField, Model, ForeignKey, NOT_PROVIDED, TextChoices

from student_group.models import StudentGroup


class Schedule(Model):
    group_user = ForeignKey(StudentGroup, on_delete=NOT_PROVIDED)
    subject = CharField(max_length=120, null=True)
    teacher = CharField(max_length=120, null=True)

    class DayOfWeekChoices(TextChoices):
        Monday = ('1Понедельник', 'Понедельник')
        Tuesday = ('2Вторник', 'Вторник')
        Wednesday = ('3Среда', 'Среда')
        Thursday = ('4Четверг', 'Четверг')
        Friday = ('5Пятница', 'Пятница')
        Saturday = ('6Суббота', 'Суббота')

    day_of_week = CharField(
        max_length=25,
        choices=DayOfWeekChoices.choices,
        default=DayOfWeekChoices.Monday,
    )

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

    def __str__(self):
        return self.subject
