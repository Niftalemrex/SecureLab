from django.contrib import admin

from .models import LabTest


@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "description")