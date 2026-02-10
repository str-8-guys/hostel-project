from django.shortcuts import render, redirect
from django.http import JsonResponse
from decimal import Decimal
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
            booking = form.save(commit=False)
            
          
            room_id = request.POST.get('room')
            try:
                room = Room.objects.get(id=room_id)
                booking.room = room
                
      
                nights = (booking.check_out - booking.check_in).days
                
                if nights > 0:
                    booking.total_price = room.price_per_night * nights
                    booking.save()
                    return redirect('booking_list')
                else:
                    form.add_error('check_out', 'Дата выезда должна быть позже даты заезда')
            except Room.DoesNotExist:
                form.add_error(None, 'Номер не найден')
    else:
        form = BookingForm()
    
    existing_guests = Guest.objects.all()
    

    rooms_with_prices = []
    for room in Room.objects.filter(is_available=True):
        rooms_with_prices.append({
            'id': room.id,
            'number': room.number,
            'type': room.get_room_type_display(),
            'price': float(room.price_per_night),
        })
    
    return render(request, 'hostel/create_booking.html', {
        'form': form,
        'existing_guests': existing_guests,
        'rooms_with_prices': rooms_with_prices,
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


def get_room_price(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
        return JsonResponse({
            'success': True,
            'price': float(room.price_per_night),
            'room_number': room.number,
            'room_type': room.get_room_type_display(),
            'currency': '₽'
        })
    except Room.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Номер не найден'}, status=404)