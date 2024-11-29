from django.db.models import CASCADE
from django.db.models.fields.related import ForeignKey
from djongo.models import (
    Model,
    AutoField,
    IntegerField,
)

from bookit_api.models.business import Business
from bookit_api.models.service import Service


class BusinessService(Model):
    businessservice_id = AutoField(primary_key=True)
    service_id = ForeignKey(Service, on_delete=CASCADE)
    business_id = ForeignKey(Business, on_delete=CASCADE)
    price = IntegerField(null=False, blank=False)
    time = IntegerField(null=False)