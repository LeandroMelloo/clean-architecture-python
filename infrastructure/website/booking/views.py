from django.shortcuts import render
from datetime import datetime, timedelta
from booking_service.application.booking.booking_services import BookingService
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto

def home(request):
    customer_dto = CustomerDto()
    customer_dto.name = 'Customer'
    dto = BookingDto(datetime.today(), datetime.today() - timedelta(days=1), customer_dto)
    response = BookingService().create_new_booking(dto)
    return render(request, 'teste.html', {'response': response})