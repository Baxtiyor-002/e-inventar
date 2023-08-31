from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Type, Handler, Structure, Device, Company
# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "inventar", "price", "handler", "structure", "document", )
    list_display_links = ("id", "name",)
    list_filter = ("type", "handler", "structure",)
    readonly_fields = ("qr_code", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.qr_code.url} width="250" height="250"')

    get_image.short_description = "QR код"


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Structure)
class StructureAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


admin.site.site_title = "E-INVENTAR | ADMINISTRATION PANEL"
admin.site.site_header = "E-INVENTAR | ADMINISTRATION PANEL"

