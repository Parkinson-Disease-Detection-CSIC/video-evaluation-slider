# Generated by Django 3.2.9 on 2021-11-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20211125_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='time_spent_general',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='time_spent_symptoms',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
