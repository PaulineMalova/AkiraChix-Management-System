# Generated by Django 2.2.1 on 2019-06-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190528_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]
