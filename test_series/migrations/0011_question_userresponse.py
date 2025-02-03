# Generated by Django 4.2.11 on 2024-07-30 10:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_series', '0010_remove_userresponse_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_no', models.IntegerField(unique=True)),
                ('question_name', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=255)),
                ('option2', models.CharField(max_length=255)),
                ('option3', models.CharField(max_length=255)),
                ('option4', models.CharField(max_length=255)),
                ('time_limit', models.DurationField(default=datetime.timedelta(seconds=30))),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_series.exam')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_series.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
