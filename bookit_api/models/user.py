from django.db.models import CASCADE
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    CharField,
    DateTimeField,
    EmailField
)

from bookit_api.models import Business


class User(Model):
    name = CharField(max_length=100, null=False, blank=False)
    email = EmailField(unique=True)
    created_at = DateTimeField(auto_now_add=True)
    phone_number = CharField(max_length=20, null=False, blank=False)
    role = CharField(max_length=20, choices = [('Client', 'Client'), ('Employee', 'Employee')])
    business = ForeignKey(Business, on_delete=CASCADE, null=True, blank=True)
