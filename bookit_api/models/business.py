from djongo.models import (
    Model,
    AutoField,
    CharField,
    DateTimeField,
    DecimalField,
)


class Business(Model):
    business_id = AutoField(primary_key=True)
    name = CharField(max_length=100,null=False, blank=False)
    address = CharField(max_length=100, null=False, blank=False)
    latitude = DecimalField(max_digits=15, null=False, blank=False)
    longitude = DecimalField(max_digits=15, null=False, blank=False)
    rating = DecimalField(max_digits=3, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
