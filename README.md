 🏨 Hostel Management System

![Django](https://img.shields.io/badge/Django-6.0-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/License-MIT-orange)

A comprehensive Django-based web application for managing hostel operations including room bookings, guest management, and real-time availability tracking.

## ✨ Features

- **🏠 Room Management** - Add, edit, and view rooms with real-time availability
- **👥 Guest Registration** - Online guest registration system
- **📅 Booking System** - Full booking management with date selection
- **🔍 Advanced Filters** - Filter rooms by type, price, and availability
- **📊 Live Statistics** - Real-time dashboard with key metrics
- **🎨 Modern UI** - Responsive design with Bootstrap 5
- **🔐 Admin Panel** - Full control through Django admin

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/str-8-guys/hostel-project.git
   cd hostel-project

Create virtual environment

bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Configure database

bash
python manage.py migrate
python manage.py createsuperuser
Run development server

bash
python manage.py runserver
Access the application

🌐 Main site: http://localhost:8000

⚙️ Admin panel: http://localhost:8000/admin

📖 API docs: http://localhost:8000/api/

📁 Project Structure
text
hostel-project/
├── hostel/                  # Main Django application
│   ├── models.py           # Database models (Room, Guest, Booking)
│   ├── views.py            # View functions
│   ├── forms.py            # Django forms
│   ├── urls.py             # URL routing
│   └── admin.py            # Admin configuration
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   └── hostel/            # App templates
│       ├── index.html     # Home page
│       ├── rooms.html     # Room listing
│       ├── bookings.html  # Booking management
│       └── register_guest.html  # Guest registration
├── static/                 # Static files
│   ├── css/style.css      # Custom styles
│   └── js/script.js       # JavaScript
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
└── README.md              # This file
🗄️ Database Models
Room Model
number - Room number (unique)

room_type - Dorm/Private/Deluxe

capacity - Maximum guests

price_per_night - Room rate

is_available - Availability status

Guest Model
name - Full name

email - Contact email (unique)

phone - Phone number

document_id - ID document number

Booking Model
room - ForeignKey to Room

guest - ForeignKey to Guest

check_in/check_out - Booking dates

total_price - Calculated price

status - Booking status

🎮 Usage Guide
For Guests
Browse rooms - Visit /rooms/ to see available rooms

Register - Click ""Register"" in navigation to create account

Book a room - Go to /bookings/create/ to make reservation

View bookings - Check /bookings/ for your reservations

For Administrators
Access admin panel - /admin/ with superuser credentials

Manage data - Add/edit rooms, guests, bookings

View statistics - Dashboard with key metrics

🔧 API Endpoints
Endpoint	Method	Description
/api/rooms/	GET	List all rooms
/api/rooms/<id>/	GET	Room details
/api/bookings/	GET/POST	List/Create bookings
/api/guests/	GET/POST	List/Create guests
🧪 Running Tests
bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test hostel

# Run with coverage
coverage run manage.py test
coverage report
