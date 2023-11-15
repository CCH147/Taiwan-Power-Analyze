from django.contrib import admin
from .models import alldata,enddate
# Register your models here.

class alldataAdmin(admin.ModelAdmin):
    list_display = ('year', 'season', 'area', 'self_avg', 'industry_avg')
admin.site.register(alldata, alldataAdmin)

class enddateAdmin(admin.ModelAdmin):
    list_display = ('year', 'month')
admin.site.register(enddate, enddateAdmin)