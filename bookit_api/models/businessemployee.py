from django.db.models import CASCADE
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    AutoField,
    BooleanField
)

from bookit_api.models import Business, User


class BusinessEmployee(Model):
    businessuser_id = AutoField(primary_key=True)
    business_id = ForeignKey(Business, on_delete=CASCADE)
    employee_id = ForeignKey(User, limit_choices_to={'role': 'employee'})
    is_admin = BooleanField(default=False)