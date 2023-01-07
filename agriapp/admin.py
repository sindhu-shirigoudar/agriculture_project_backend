from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ContactDetails)
admin.site.register(models.Devise)
admin.site.register(models.DeviseApis)
admin.site.register(models.DeviseLocation)
admin.site.register(models.APICountThreshold)