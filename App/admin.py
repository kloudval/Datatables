from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'occupation', 'gender']
    list_per_page = 8
    search_fields = ['name', 'email']


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
