from django.db import models
from decimal import Decimal  

class Room(models.Model):
    ROOM_TYPES = [
        ('dorm', 'Общий номер'),
        ('private', 'Приватный номер'),
        ('deluxe', 'Делюкс номер'),
    ]
    
    number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Номер {self.number} ({self.get_room_type_display()})"
    
    def calculate_price(self, nights):  
        """Рассчитать стоимость проживания"""
        if nights <= 0:
            return Decimal('0.00')
        

        return self.price_per_night * nights
    
    def get_nights(self, check_in, check_out):
        """Получить количество ночей между датами"""
        if not check_in or not check_out:
            return 0
        
        days = (check_out - check_in).days
        return max(days, 0)


class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    document_id = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('confirmed', 'Подтверждено'),
        ('checked_in', 'Заселен'),
        ('checked_out', 'Выселен'),
        ('cancelled', 'Отменено'),
    ], default='confirmed')
    
    def __str__(self):
        return f"Бронирование #{self.id} - {self.guest.name}"
    
   
    def calculate_and_save_price(self):
        """Рассчитать и сохранить цену автоматически"""
        nights = (self.check_out - self.check_in).days
        if nights > 0:
            self.total_price = self.room.price_per_night * nights
            self.save()
        return self.total_price