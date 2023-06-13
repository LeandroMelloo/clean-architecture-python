from django.shortcuts import render
from datetime import datetime
from service.application.booking.services import BookingService
from service.application.booking.dto import BookingDto
from service.application.customers.dto import CustomerDto
from infrastructure.website.booking.repositories import BookingRepository


def home(request):
    return render(request, "index.html")


def create_new(request):
    checkin = datetime.strptime(
        request.POST.get("checkin"), "%Y-%m-%dT%H:%M"
    )
    checkout = datetime.strptime(
        request.POST.get("checkout"), "%Y-%m-%dT%H:%M"
    )
    name = request.POST.get("name")
    age = int(request.POST.get("age"))
    document = request.POST.get("document")
    email = request.POST.get("email")

    customer_dto = CustomerDto(name, age, document, email)
    dto = BookingDto(checkin, checkout, customer_dto)
    repository = BookingRepository()
    service = BookingService(repository)
    response = service.create_new_booking(dto)

    if response["code"] != "SUCCESS":
        return render(request, "index.html", {"response": response})
    else:
        return render(request, "confirmation.html")
