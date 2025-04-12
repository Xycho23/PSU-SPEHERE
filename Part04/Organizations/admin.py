from django.contrib import admin
from .models import Organizations

@admin.register(Organizations)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at') 
