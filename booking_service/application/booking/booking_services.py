from booking_service.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import ErrorCodes


"""Use Cases"""
class BookingManager(object):
    def create_new_booking(self, bookingDto: BookingDto):
        domain_object = bookingDto.to_domain() # transformando o BookingDto em um objeto de dominio

        try:
            if domain_object.is_valid():
                return 'save'
            else:
                return 'dont save'
        except CheckinDateCannotBeAfterCheckoutDate as e:
            return { 'message': e.message, 'code': ErrorCodes.CHECKINAFTERCHECKOUT }
        except Exception as e:
            return {'message': e.message, 'code': ErrorCodes.UNDEFINED }
        
        