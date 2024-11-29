from django.db.models import CASCADE
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    AutoField,
    CharField,
    DateTimeField,
)

from bookit_api.models import Business
from bookit_api.models.user import User


class Booking(Model):
    booking_id = AutoField(primary_key=True)
    business_id = ForeignKey(Business, on_delete=CASCADE)
    client_id = ForeignKey(User, on_delete=CASCADE, limit_choices_to={'role': 'Client'})
    employee_id = ForeignKey(User, on_delete=CASCADE, limit_choices_to={'role': 'Employee'})
    booking_date = DateTimeField(null=False, blank=False)
    status = CharField(
        max_length=15, null=False, choices=[
            ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')
        ]
    )