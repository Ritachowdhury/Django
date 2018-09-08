from django.contrib import admin
from .models import Divisions,Districts

# Register your models here.

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name','population','area')

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','education_rate','population_density','visited','division')

admin.site.register(Divisions,DivisionAdmin)
admin.site.register(Districts,DistrictAdmin)