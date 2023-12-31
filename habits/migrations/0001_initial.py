# Generated by Django 4.2.4 on 2023-08-21 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NiceHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='место')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='название')),
                ('durations', models.SmallIntegerField(default=10, verbose_name='продолжительность')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'приятная привычка',
                'verbose_name_plural': 'приятные привычки',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='место')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время')),
                ('action', models.CharField(max_length=100, verbose_name='название')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение')),
                ('durations', models.SmallIntegerField(default=10, verbose_name='продолжительность')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная')),
                ('nice_habit', models.ManyToManyField(blank=True, null=True, to='habits.nicehabit', verbose_name='приятная привычка')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'полезная привычка',
                'verbose_name_plural': 'полезные привычки',
                'ordering': ('title',),
            },
        ),
    ]
