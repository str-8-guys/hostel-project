from django.shortcuts import render
from .models import Room, Booking

def index(request):
    return render(request, 'hostel/index.html')
def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'hostel/rooms.html', {'rooms': rooms})

def booking_list(request):
    bookings = Booking.objects.all().order_by('-check_in')
    return render(request, 'hostel/bookings.html', {'bookings': bookings})