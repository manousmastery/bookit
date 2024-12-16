from djongo import models


class BusinessServiceDetails(models.Model):
    businessservice_id = models.AutoField(primary_key=True)
    price = models.FloatField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    showed_name = models.CharField(blank=True, null=True, max_length=255)
    showed_description = models.TextField(blank=True, null=True, max_length=255)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'business',
            'service',
        )  # Ensures unique combination of business and service
