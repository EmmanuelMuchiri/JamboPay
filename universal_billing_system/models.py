from django.db import models

# Create your models here.
class Industry(models.Model):
    name = models.CharField( blank=False,max_length= 40,default='JamboPay')
    def __str__(self):
        return self.name  
class Merchant(models.Model):
    Business_name = models.CharField(max_length=20,blank=False)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60,blank=False)
    Physical_address = models.CharField(max_length=60,blank=False)
    Post_code = models.CharField(max_length=20,blank=False)
    Town = models.CharField(max_length=20,blank=False)
    Industry = models.ForeignKey(Industry,null=False)
    JP_paybill = models.CharField(max_length=20,blank=False)


class Town(models.Model):
    # Town_id = models.PrimaryKey(Id,null=True,blank=False)
    Merchant = models.ForeignKey(Merchant,null=False,blank=False)





