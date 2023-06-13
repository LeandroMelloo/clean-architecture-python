from service.application.booking.storage import BookingStorage
from service.domain.booking.exceptions import (
    CheckinDateCannotBeAfterCheckoutDate,
    CustomerCannotBeBlank,
)
from service.domain.customers.exceptions import (
    CustomerShouldBeOlderThan18,
    InvalidCustomerDocumentException,
)
from .dto import BookingDto
from service.domain.booking.enums import ErrorCodes, SuccessCodes


class BookingService(object):
    storage: BookingStorage

    def __init__(self, storage: BookingStorage) -> None:
        self.storage = storage

    def create_new_booking(self, bookingDto: BookingDto):
        booking_aggregate = bookingDto.to_domain()

        try:
            booking_aggregate.close_booking()
            final_dto = bookingDto.to_dto(booking_aggregate)
            self.storage.save_booking(final_dto)
            return {
                "message": SuccessCodes.SUCCESS.value,
                "code": SuccessCodes.SUCCESS.name,
            }
        except CheckinDateCannotBeAfterCheckoutDate:
            return {
                "message": ErrorCodes.CHECKINAFTERCHECKOUT.value,
                "code": ErrorCodes.CHECKINAFTERCHECKOUT.name,
            }
        except CustomerCannotBeBlank:
            return {
                "message": ErrorCodes.CUSTOMERISREQUIRED.value,
                "code": ErrorCodes.CUSTOMERISREQUIRED.name,
            }
        except CustomerShouldBeOlderThan18:
            return {
                "message": ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.value,
                "code": ErrorCodes.CUSTOMERSHOULDBEOLDERTHAN18.name,
            }
        except InvalidCustomerDocumentException:
            return {
                "message": ErrorCodes.INVALIDCUSTOMERDOCUMENT.value,
                "code": ErrorCodes.INVALIDCUSTOMERDOCUMENT.name,
            }
        except Exception as e:
            print(e)
            return {
                "message": ErrorCodes.UNDEFINED.value,
                "code": ErrorCodes.UNDEFINED.name,
            }
