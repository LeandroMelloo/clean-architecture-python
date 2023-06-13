from enum import Enum


class ErrorCodes(Enum):
    MSG_ERROR_DELETE = "Booking with this status does not allow delete"
    CHECKINAFTERCHECKOUT = "Checkin date cannot be after checkout"
    CUSTOMERISREQUIRED = "Customer is required"
    CUSTOMERSHOULDBEOLDERTHAN18 = "Customer should be older than 18"
    INVALIDCUSTOMERDOCUMENT = "Invalid customer document"
    USERNOTALLOWEDTOACCESSDATA = "User not allowed to access this data"
    UPDATEBOOKINGREQUIRESBOOKINGID = "Cannot update a booking without its id"
    BOOKINGSTATUSDOESNOTALLOWDELETE = MSG_ERROR_DELETE
    UNDEFINED = "Undefined"


class SuccessCodes(Enum):
    SUCCESS = "Success"


class BookingStatus(Enum):
    OPEN = 0
    RESERVED = 1
    FINISHED = 2
    CANCELED = 3
    DELETED = 4
