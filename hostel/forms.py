from django import forms
from .models import Booking, Room, Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'phone', 'document_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'document_id': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'guest', 'check_in', 'check_out', 'total_price']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'guest': forms.Select(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }