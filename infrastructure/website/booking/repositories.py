from service.application.booking.dto import BookingDto
from service.application.booking.storage import BookingStorage
from service.application.customers.dto import CustomerDto
from booking.models import Booking, Customer
from django.db import transaction


class BookingRepository(BookingStorage):
    def _customer_dto_to_model(self, customerDto: CustomerDto):
        customer = Customer()
        customer.name = customerDto.name
        customer.age = customerDto.age
        customer.document = customerDto.document
        customer.email = customerDto.email

        return customer

    def _booking_dto_to_model(self, bookingDto: BookingDto):
        booking = Booking()
        booking.checkin = bookingDto.checkin
        booking.checkout = bookingDto.checkout

        return booking

    @transaction.atomic
    def save_booking(self, bookingDto: BookingDto):
        customer = self._customer_dto_to_model(bookingDto.customer)
        customer.save()
        booking = self._booking_dto_to_model(bookingDto)
        booking.customer = customer
        booking.save()
