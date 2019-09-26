from django.db import models

# Create your models here.
class Industry(models.Model):
    name = models.CharField( blank=False,max_length= 40,default='JamboPay')
    def __str__(self):
        return self.name 
class Category(models.Model):
    name = models.CharField( blank=False,max_length= 40,default='JamboPay')
    def __str__(self):
        return self.name                    
class Revstreams(models.Model):
    name = models.CharField( blank=False,max_length= 40,default='JamboPay')
    # Category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
class Merchant(models.Model):
    Business_name = models.CharField(max_length=20,blank=False)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=60,blank=False)
    Physical_address = models.CharField(max_length=60,blank=False)
    Post_code = models.CharField(max_length=20,blank=False)
    Town = models.CharField(max_length=20,blank=False)
    JP_paybill = models.CharField(max_length=20,blank=False)
    Industry = models.ManyToManyField(Industry)
    Revstreams = models.ManyToManyField(Revstreams)
    
    def __str__(self):
        return self.name

class Bills(models.Model):
    customer_name = models.CharField(max_length=255,blank=False)
    customer_phone = models.CharField(max_length=255,blank=False)
    customer_email = models.EmailField(max_length=255,blank=False)
    Revstreams = models.CharField(max_length=255,blank=False)
    narration = models.CharField(max_length=255,blank=False)
    amount = models.FloatField(blank=False)
    quantity = models.FloatField(blank=True)







