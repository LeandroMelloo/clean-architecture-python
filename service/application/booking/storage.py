from abc import ABC, abstractclassmethod
from .dto import BookingDto


class BookingStorage(ABC):
    @abstractclassmethod
    def save_booking(self, bookingDto: BookingDto):
        pass
