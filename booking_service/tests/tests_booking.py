import unittest
from datetime import datetime, timedelta
import sys

sys.path.append("..")
sys.path.append("../../")
from booking_service.domain.booking.entities import Booking
from booking_service.domain.customers.entities import Customer
from booking_service.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank
from booking_service.domain.customers.exceptions import InvalidCustomerDocumentException
from booking_service.application.booking.booking_services import BookingService
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto


class BookingTests(unittest.TestCase):

    def test_checkin_date_cannot_be_after_checkout_date(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        with self.assertRaises(CheckinDateCannotBeAfterCheckoutDate) as ex:
            booking.is_valid()

        exception = ex.exception
        self.assertEqual(exception.message, "Checkin cannot be after Checkout")

    def test_checkin_date_cannot_be_after_checkout_date2(self):
        checkin = datetime.utcnow()
        checkout = datetime.today() - timedelta(days=1)
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertRaises(CheckinDateCannotBeAfterCheckoutDate, booking.is_valid)

    def test_checkin_date_cannot_be_after_checkout_date3(self):
        checkin = datetime.utcnow()
        checkout = datetime.today() - timedelta(days=1)
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)

        self.assertEqual(response['code'], 'CHECKINAFTERCHECKOUT')

    def test_customer_cannot_be_blank(self):
        checkin = datetime.today()
        checkout = datetime.today()
        booking = Booking(checkin=checkin, checkout=checkout, customer=None)

        self.assertRaises(CustomerCannotBeBlank, booking.is_valid)

    def test_customer_must_have_valid_document(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = Customer("Customer", 18, "123", "a@a.com")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertRaises(InvalidCustomerDocumentException, booking.is_valid)

    def test_customer_happy_path(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = Customer("Customer", 18, "12356", "a@a.com")
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertTrue(booking.is_valid())
    
    def test_create(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("Customer", 18, "doc123", "a@a.com")
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response['code'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()