# Generated by Django 3.1.12 on 2024-12-15 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookit_api', '0008_auto_20241207_2339'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='businessservicedetails',
            unique_together={('business', 'service')},
        ),
    ]