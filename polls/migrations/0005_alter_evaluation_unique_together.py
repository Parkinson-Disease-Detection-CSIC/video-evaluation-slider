# Generated by Django 3.2.9 on 2021-11-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211117_1448'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluation',
            unique_together={('evaluator', 'subject')},
        ),
    ]