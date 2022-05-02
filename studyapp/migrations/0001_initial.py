# Generated by Django 4.0.2 on 2022-05-02 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('department', models.CharField(default='DEP', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default=None, max_length=400)),
                ('start_time', models.DateTimeField(default=None, verbose_name='Start time')),
                ('end_time', models.DateTimeField(default=None, verbose_name='End time')),
                ('post_text', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date posted')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyapp.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('enrolled_courses', models.CharField(max_length=200)),
                ('selected_courses', models.CharField(max_length=200)),
                ('friends', models.ManyToManyField(to='studyapp.Profile')),
                ('meetings', models.ManyToManyField(to='studyapp.Meeting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='buddies',
            field=models.ManyToManyField(to='studyapp.Profile'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='studyapp.course'),
        ),
        migrations.CreateModel(
            name='Friend_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='studyapp.profile')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='studyapp.profile')),
            ],
        ),
    ]
