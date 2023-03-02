from django.contrib import admin
from .models import Health


# Register your models here.
@admin.register(Health)
class HealthAdmin(admin.ModelAdmin):
    list_display = (
        "health",
        "icon",
    )
