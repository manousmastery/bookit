from django.db.models import Model, AutoField, CharField


class Service(Model):
    service_id = AutoField(primary_key=True)
    name = CharField(max_length=100,null=False, blank=False, unique=True)
    description = CharField(max_length=200, blank=True)
