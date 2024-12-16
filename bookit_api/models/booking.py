from djongo import models


class Booking(models.Model):
    BOOKING_STATUS = [
        ('COMPLETED', 'Completed'),
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
    ]
    booking_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('User', on_delete=models.CASCADE, related_name='client_bookings')
    employee = models.ForeignKey('User', on_delete=models.CASCADE, related_name='employee_bookings')
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(null=False)
    status = models.CharField(max_length=10, null=False, choices=BOOKING_STATUS)