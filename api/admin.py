from django.contrib import admin
from .import models

# Register your models here.
class AdminArea(admin.AdminSite):
    site_header ='Admin Site'

admin_site =AdminArea(name='Admin Site')


admin_site.register(models.User)
admin.site.register(models.User)
