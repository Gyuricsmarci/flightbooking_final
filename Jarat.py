from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, flightNumber, flightType, maxPassanger, flightOrigin, flightDestiantion, flightPrice, flightStart):
        self.flightNumber = flightNumber
        self.flightType = flightType
        self.maxPassanger = maxPassanger
        self.flightOrigin = flightOrigin
        self.flightDestination = flightDestiantion
        self.flightPrice = flightPrice
        self.flightStart = flightStart
        self.numberOfBooking = 0