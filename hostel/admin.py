from django.contrib import admin
from .models import Room, Guest, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number', 'room_type', 'capacity', 'price_per_night', 'is_available']
    list_filter = ['room_type', 'is_available']
    search_fields = ['number', 'description']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email', 'document_id']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'guest', 'room', 'check_in', 'check_out', 'status']
    list_filter = ['status', 'check_in']
    search_fields = ['guest__name', 'room__number']