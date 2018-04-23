from django.contrib import admin

# Register your models here.

from app2.models import *

class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ['name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'school']
    search_fields = ['name']

admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)
