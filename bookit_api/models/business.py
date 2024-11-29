from djongo import models

class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False, blank=False)
    address = models.CharField(max_length=100,null=False, blank=False)

class BusinessDomain(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False, blank=False, unique=True)

class BusinessDomainService(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.ForeignKey(BusinessDomain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False, blank=False,unique=True)
    
class BusinessDomainAssociation(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    domain = models.ForeignKey(BusinessDomain, on_delete=models.CASCADE)
