# Generated by Django 4.1.2 on 2022-10-23 08:14

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student_group', '0001_initial'),
        ('users', '0002_auto_20221021_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='edu_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.fields.NOT_PROVIDED, to='student_group.studentgroup'),
        ),
    ]
