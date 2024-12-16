from djongo import models


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE)
    description = models.TextField()
