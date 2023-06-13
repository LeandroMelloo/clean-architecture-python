import unittest
from datetime import datetime, timedelta
import sys
sys.path.append("..")
sys.path.append("../../")
from booking_service.domain.booking.exceptions import *
from booking_service.domain.customers.exceptions import *
from booking_service.application.booking.booking_services import BookingService
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto


class BookingTests(unittest.TestCase):

    def test_checkin_date_cannot_be_after_checkout_date(self):
        checkin = datetime.today()
        checkout = datetime.today() - timedelta(days=1)
        customer = CustomerDto('Leandro', 37, 'doctest123', 'leandroteste@gmail.com')
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response['code'], 'CHECKINAFTERCHECKOUT')

    def test_customer_should_older_than_18(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto('Leandro', 17, 'doctest123', 'leandroteste@gmail.com')
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response['code'], 'CUSTOMERSHOULDBEOLDERTHAN18')

    def test_customer_invalid_document(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto('Leandro', 37, 'doct', 'leandroteste@gmail.com')
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response['code'], 'INVALIDCUSTOMERDOCUMENT')

    def test_create(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto('Leandro', 37, 'doctest123', 'leandroteste@gmail.com')
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        service = BookingService()
        response = service.create_new_booking(booking_dto)
        self.assertEqual(response['code'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()