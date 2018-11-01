from django.contrib import admin
from .models import Person, Commodity, Method


class PersonAdmin(admin.ModelAdmin):
    ordering = ['initials']


class CommodityAdmin(admin.ModelAdmin):
    ordering = ['commodity']


class MethodsAdmin(admin.ModelAdmin):
    ordering = ['method']

# Register your models here.
admin.site.register(Person, PersonAdmin)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Method, MethodsAdmin)