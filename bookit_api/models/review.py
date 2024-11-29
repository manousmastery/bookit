from django.db.models import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    AutoField,
    DateTimeField,
    IntegerField,
)

from bookit_api.models.user import User
from bookit_api.models.businessservice import BusinessService


class Review(Model):
    reviewId = AutoField(primary_key=True)
    businessService = ForeignKey(BusinessService, on_delete=CASCADE)
    client_id = ForeignKey(User, on_delete=CASCADE, limit_choices_to={'role': 'Client'})
    rating = IntegerField()
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)