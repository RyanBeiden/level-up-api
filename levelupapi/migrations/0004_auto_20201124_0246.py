# Generated by Django 3.1.3 on 2020-11-24 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20201124_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_time',
            new_name='time',
        ),
    ]