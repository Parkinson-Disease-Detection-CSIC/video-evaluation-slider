# Generated by Django 3.2.9 on 2021-11-17 15:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_evaluation_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluation',
            name='date',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='general_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='evaluation date for general'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evaluation',
            name='symptoms_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='evaluation date for symptoms'),
            preserve_default=False,
        ),
    ]
