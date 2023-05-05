from .exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank
from datetime import datetime
from booking_service.domain.customers.entities import Customer
from booking_service.domain.rooms.entities import Room


"""conceito de aggregate, composto de diversas entidades"""
class Booking(object):
    """propriedades do objeto"""
    checkin: datetime
    checkout: datetime
    customer: Customer
    profit_margin: float
    room: Room

    """instânciando o objeto e setando cada uma das propriedades"""
    def __init__(self, checkin: datetime, checkout: datetime, customer: Customer):
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer

    """Logica de negocio"""
    def close_booking(self):
        self.is_valid()

    def is_valid(self):
        if self.checkin > self.checkout:
            raise CheckinDateCannotBeAfterCheckoutDate("Checkin cannot be after checkout")
        elif self.customer:
            raise CustomerCannotBeBlank("Customer is a required information")

        return True