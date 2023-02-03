from django.contrib import admin
from .models import Type, Handler, Structure, Device, Company
# Register your models here.


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "inventar", "price", "handler", "structure")
    list_display_lin = ("id", "name", "inventar", "price", "handler", "structure")

admin.site.register(Type)
admin.site.register(Handler)
admin.site.register(Structure)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Company)