# Generated by Django 3.2.9 on 2021-11-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20211117_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='done_general',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='done_symptoms',
            field=models.BooleanField(default=False),
        ),
    ]