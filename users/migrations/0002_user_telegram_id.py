# Generated by Django 4.2.4 on 2023-08-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telegram_id',
            field=models.IntegerField(default=308445161, verbose_name='telegram id'),
            preserve_default=False,
        ),
    ]