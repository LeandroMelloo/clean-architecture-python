import unittest
from datetime import datetime, timedelta
import sys
sys.path.append("..")
sys.path.append("../../")
from booking_service.domain.booking.entities import Booking
from booking_service.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate
from booking_service.domain.customers.entities import Customer
from booking_service.application.booking.booking_services import BookingService
from booking_service.application.booking.booking_dto import BookingDto



class BookingTests(unittest.TestCase):

    def test_checkin_date_cannot_be_after_checkout_date(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
        customer = Customer()
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        with self.assertRaises(CheckinDateCannotBeAfterCheckoutDate) as ex:
            booking.is_valid()

        exception = ex.exception
        self.assertEqual(exception.message, "Checkin cannot be after Checkout")

    def test_checkin_date_cannot_be_after_checkout_date2(self):
        checkin = datetime.utcnow()
        checkout = datetime.today() - timedelta(days=1)
        customer = Customer()
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertRaises(CheckinDateCannotBeAfterCheckoutDate, booking.is_valid)
    
    def test_create(self):
        checkin = datetime.utcnow()
        checkout = datetime.today()
        customer = Customer()
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response, 'save')

if __name__ == '__main__':
    unittest.main()