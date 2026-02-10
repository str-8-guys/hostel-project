from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.create_booking, name='create_booking'),
]