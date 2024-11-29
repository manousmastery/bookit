from djongo import models
from .business import Business
from .user import User

class BusinessUserAssociation(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)