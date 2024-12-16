from djongo import models


class ServiceCategory(models.Model):
    servicecategory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
