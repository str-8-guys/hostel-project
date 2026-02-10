from django.shortcuts import render, redirect
from .models import Room, Booking, Guest
from .forms import BookingForm  

def index(request):
    context = {
        'room_count': Room.objects.count(),
        'guest_count': Guest.objects.count(),
        'booking_count': Booking.objects.count(),
        'available_rooms': Room.objects.filter(is_available=True).count(),
    }
    return render(request, 'hostel/index.html', context)

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hostel/rooms.html', {'rooms': rooms})

def room_list(request):
    room_type = request.GET.get('room_type', '')
    min_price = request.GET.get('min_price', '')
    
    rooms = Room.objects.filter(is_available=True)
    
    if room_type:
        rooms = rooms.filter(room_type=room_type)
    if min_price:
        rooms = rooms.filter(price_per_night__gte=min_price)
    
    return render(request, 'hostel/rooms.html', {
        'rooms': rooms,
        'selected_type': room_type,
        'selected_min_price': min_price,
    })

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
    
    return render(request, 'hostel/create_booking.html', {'form': form})