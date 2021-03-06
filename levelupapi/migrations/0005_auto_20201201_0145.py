# Generated by Django 3.1.3 on 2020-12-01 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0004_auto_20201124_0246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.CreateModel(
            name='GamerEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.event')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer')),
            ],
        ),
    ]
