from django.contrib import admin
from .models import JobCard

@admin.register(JobCard)
class JobCardAdmin(admin.ModelAdmin):
    list_display = ('job_card_no', 'full_name', 'phone_number', 'status', 'payment_status', 'timestamp')
    search_fields = ('job_card_no', 'full_name', 'registration_number')
    list_filter = ('status', 'payment_status', 'preferred_service_date')
