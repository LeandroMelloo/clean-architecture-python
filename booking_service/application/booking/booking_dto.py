from datetime import datetime
from booking_service.domain.booking.entities import Booking
from booking_service.domain.booking.entities import Customer
from booking_service.application.customers.customer_dto import CustomerDto


class BookingDto(object):
    """propriedades do objeto"""
    checkin: datetime
    checkout: datetime
    customer: Customer

    """instânciando o objeto e setando cada uma das propriedades"""
    def __init__(self, checkin: datetime, checkout: datetime, customer: CustomerDto):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    """função especifica para transformar de DTO para Dominio"""
    def to_domain(self):
        return Booking(self.checkin, self.checkout, self.customer)