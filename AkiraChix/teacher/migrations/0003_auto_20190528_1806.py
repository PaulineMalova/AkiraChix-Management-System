# Generated by Django 2.2.1 on 2019-05-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_number',
            field=models.IntegerField(),
        ),
    ]
