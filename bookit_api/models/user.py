from djongo import models
from .business import Business

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True)
    is_business_member = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)