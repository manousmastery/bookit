# Generated by Django 3.1.12 on 2024-12-16 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookit_api', '0009_auto_20241215_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='business_service_details',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='bookit_api.businessservicedetails'),
            preserve_default=False,
        ),
    ]