# Generated by Django 3.1.12 on 2024-12-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookit_api', '0007_booking_businessservicedetails_review_schedule_service_servicecategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='category',
        ),
        migrations.AddField(
            model_name='servicecategory',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
