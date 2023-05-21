from datetime import datetime
from booking_service.domain.booking.entities import Booking
from booking_service.application.customers.customer_dto import CustomerDto

class BookingDto(object):
    id: int
    checkin: datetime
    checkout: datetime
    customer: CustomerDto

    def __init__(self, checkin: datetime, checkout: datetime, customer: CustomerDto):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    def to_domain(self):
        booking = Booking(self.checkin, self.checkout, self.customer.to_domain())
        return booking

    def to_dto(self, booking: Booking):
        customer_dto = self.customer.to_dto(booking.customer)
        booking_dto = BookingDto(
            checkin=booking.checkin, 
            checkout=booking.checkout, 
            customer=customer_dto)
        return booking_dto