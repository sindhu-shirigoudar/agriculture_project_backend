from django.db import models

# Create your models here.

class ContactDetails(models.Model):
    name       = models.CharField(max_length=255)
    phone      = models.CharField(max_length=255, unique=True)
    mail       = models.EmailField(unique=True)
    message    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Devise(models.Model):
    name          = models.CharField(max_length=255)
    setial_no     = models.CharField(max_length=255, unique=True)
    devise_id     = models.CharField(max_length=255, unique=True) #devise id or user name
    chipset_no    = models.CharField(max_length=255, unique=True)
    email         = models.EmailField()
    phone         = models.CharField(max_length=255)
    address1      = models.CharField(max_length=255)
    address2      = models.CharField(max_length=255)
    purchase_date = models.DateField()
    time_of_sale  = models.TimeField()
    warrenty      = models.DateField(max_length=255)
    amount_paid   = models.BigIntegerField()
    balance_amount= models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name + self.devise_id