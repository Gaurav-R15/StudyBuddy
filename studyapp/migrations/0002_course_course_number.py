# Generated by Django 4.0.2 on 2022-04-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.CharField(default='0000', max_length=5),
        ),
    ]
