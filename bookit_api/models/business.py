from djongo import models


class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=False)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=3, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)