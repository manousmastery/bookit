# Generated by Django 3.1.12 on 2024-12-06 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit_api', '0004_auto_20241206_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='address',
        ),
        migrations.RemoveField(
            model_name='business',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='business',
            name='longitude',
        ),
    ]
