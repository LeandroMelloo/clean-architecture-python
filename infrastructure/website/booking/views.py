from django.shortcuts import render
from datetime import datetime
from booking_service.application.booking.booking_services import BookingService
from booking_service.application.booking.booking_dto import BookingDto

def home(request):
    dto = BookingDto(datetime.today(), datetime.today(), "String")
    response = BookingService().create_new_booking(dto)
    return render(request, 'home.html', {'response': response})
