# Generated by Django 2.2.2 on 2019-07-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20190716_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id_number',
            field=models.BigIntegerField(),
        ),
    ]