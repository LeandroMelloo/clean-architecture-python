from booking_service.domain.booking.exceptions import *
from booking_service.domain.customers.exceptions import *
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import *

class BookingService(object):
    def create_new_booking(self, bookingDto: BookingDto):
        booking_aggregate = bookingDto.to_domain()

        try:
            if booking_aggregate.is_valid():
                return {'message': SuccessCodes.SUCCESS.value, 'code': SuccessCodes.SUCCESS.name}
        except CheckinDateCannotBeAfterCheckoutDate:
            return {'message': ErrorCodes.CHECKINAFTERCHECKOUT.value, 'code': ErrorCodes.CHECKINAFTERCHECKOUT.name}
        except CustomerCannotBeBlank:
            return {'message': ErrorCodes.CUSTOMERISREQUIRED.value, 'code': ErrorCodes.CUSTOMERISREQUIRED.name}
        except CustomerShouldBeOlderThan18:
            return {'message': ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.value, 'code': ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.name}
        except InvalidCustomerDocumentException:
            return {'message': ErrorCodes.INVALIDCUSTOMERDOCUMENT.value, 'code': ErrorCodes.INVALIDCUSTOMERDOCUMENT.name}
        except Exception:
            return {'message': ErrorCodes.UNDEFINED.value, 'code': ErrorCodes.UNDEFINED.name}
        
        