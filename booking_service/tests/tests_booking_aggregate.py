import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('..')
sys.path.append('../..')
from domain.booking.entities import Booking
from domain.booking.exceptions import *
from domain.customers.exceptions import *
from domain.customers.entities import Customer

class BookingAggregateTests(unittest.TestCase):

    def test_checkin_date_cannot_be_after_checkout_date(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
        customer = Customer('Leandro', 37, 'doctest123', 'leandroteste@gmail.com')
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        with self.assertRaises(CheckinDateCannotBeAfterCheckoutDate) as ex:
            booking.is_valid()

        exception = ex.exception
        self.assertEqual(exception.message, "Checkin cannot be after Checkout")

    def test_checkin_date_cannot_be_after_checkout_date_exception(self):
        checkin = datetime.utcnow()
        checkout = datetime.today() - timedelta(days=1)
        customer = Customer('Leandro', 37, 'doctest123', 'leandroteste@gmail.com')
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertRaises(CheckinDateCannotBeAfterCheckoutDate,  booking.is_valid)

    def test_customer_cannot_be_blank(self):
        checkin = datetime.today()
        checkout = datetime.today()
        booking = Booking(checkin=checkin, checkout=checkout, customer=None)

        self.assertRaises(CustomerCannotBeBlank,  booking.is_valid)

    def test_customer_must_have_valid_document(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = Customer('Leandro', 37, 'doct', 'leandroteste@gmail.com')
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertRaises(InvalidCustomerDocumentException,  booking.is_valid)

    def test_customer_happy_path(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = Customer('Leandro', 37, '12356', 'leandroteste@gmail.com')
        booking = Booking(checkin=checkin, checkout=checkout, customer=customer)

        self.assertTrue(booking.is_valid())

if __name__ == '__main__':
    unittest.main()