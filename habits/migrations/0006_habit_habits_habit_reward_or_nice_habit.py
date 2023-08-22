# Generated by Django 4.2.4 on 2023-08-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_nicehabit_is_public_alter_habit_action_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='habit',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('nice_habit__isnull', False), ('reward__isnull', True)), models.Q(('nice_habit__isnull', True), ('reward__isnull', False)), _connector='OR'), name='habits_habit_reward_or_nice_habit'),
        ),
    ]