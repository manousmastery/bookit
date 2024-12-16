from djongo import models


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey('User', on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)
