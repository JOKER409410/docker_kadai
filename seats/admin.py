from django.contrib import admin

from .models import Seat


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("row", "col", "occupant_name", "status", "updated_at")
    list_filter = ("status", "row")