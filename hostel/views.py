from django.shortcuts import render, redirect
from .models import Room, Booking, Guest
from .forms import BookingForm, GuestForm

def index(request):
    context = {
        'room_count': Room.objects.count(),
        'guest_count': Guest.objects.count(),
        'booking_count': Booking.objects.count(),
        'available_rooms': Room.objects.filter(is_available=True).count(),
    }
    return render(request, 'hostel/index.html', context)

def room_list(request):
    room_type = request.GET.get('room_type', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    
    rooms = Room.objects.filter(is_available=True)
    
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    if min_price:
        try:
            rooms = rooms.filter(price_per_night__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            rooms = rooms.filter(price_per_night__lte=float(max_price))
        except ValueError:
            pass
    
    context = {
        'rooms': rooms,
        'selected_type': room_type,
        'selected_min_price': min_price,
        'selected_max_price': max_price,
    }
    return render(request, 'hostel/rooms.html', context)

def booking_list(request):
    bookings = Booking.objects.all().order_by('-check_in')
    return render(request, 'hostel/bookings.html', {'bookings': bookings})

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    
    existing_guests = Guest.objects.all()
    
    return render(request, 'hostel/create_booking.html', {
        'form': form,
        'existing_guests': existing_guests,
    })

def register_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_booking')  
    else:
        form = GuestForm()
    
    return render(request, 'hostel/register_guest.html', {'form': form})