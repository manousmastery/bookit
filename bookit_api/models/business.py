from djongo import models

class Business(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)

class BusinessDomain(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False, unique=True)

class BusinessDomainService(models.Model):
    domain = models.ForeignKey(BusinessDomain, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False, blank=False,unique=True)
    
class BusinessDomainAssociation(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    domain = models.ForeignKey(BusinessDomain, on_delete=models.CASCADE)

class BusinessStaffMember(models.Model):
    name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    type = models.ForeignKey(BusinessDomain, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({'Gérant' if self.isAdmin else 'Employé'}) : {self.name}"
