from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'status', 'customer', 'created_at')
    list_filter = ('status', 'service_type')
    search_fields = ('customer__username',)