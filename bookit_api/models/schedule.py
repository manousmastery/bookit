from django.db.models import CASCADE
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    AutoField,
    CharField,
    DateTimeField,
    DateField,
    IntegerField,
    BooleanField,
)

from bookit_api.models import Business
from bookit_api.models.user import User
class Schedule(Model):
    schedule_id = AutoField(primary_key=True)
    date = DateField()
    employee_id = ForeignKey(User, on_delete=CASCADE, limit_choices_to={'role': 'Employee'})
    start_time = DateTimeField()
    end_time = DateTimeField()
    availability = BooleanField(default=False)