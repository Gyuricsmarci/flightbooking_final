from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from Legitarsasag import Legitarsasag


class JegyFoglalas:

    def __init__(self, airLine):
        self.airLine = airLine
        self._bookedFlights = []

    @property
    def bookedFlights(self):
        for foglalas in self._bookedFlights:
            print(
                f" A {foglalas[0]} azonosítójú foglalás a következő járatra érvényes: {foglalas[1].flightNumber}"
            )
            #print(len(self._bookedFlights))

    def initBookAFlight(self, id, flight):
        self._bookedFlights.append([id, flight])
        flight.numberOfBooking = flight.numberOfBooking + 1
    
    def bookAFlight(self, id, flight, mostido):
        if (flight.maxPassanger) >= (flight.numberOfBooking +
                                     1) and (flight.flightStart > mostido):
            flight.numberOfBooking += 1
            self._bookedFlights.append([id, flight])
        elif (flight.maxPassanger) < (flight.numberOfBooking + 1):
            print("A járat megtelt!")
        else:
            print("""A járatra már nem lehetséges a foglalás!
Minden járatra legkésőbb  az indulást megelőző naptári napon lehet foglalni!""")

    def cancelAFlight(self, id):
        volt_e = False
        for foglalas in self._bookedFlights:
            if id == foglalas[0]:
                foglalas[1].numberOfBooking -= 1
                self._bookedFlights.remove(foglalas)
                volt_e = True
                break
        if not volt_e:
            print("Nincs ilyen foglalás!")
            
            

    def __len__(self):
        return len(self._bookedFlights)

    def getNumberOfValidBookings(self):
        return self._bookedFlights

    def maxID(self):
        max = self._bookedFlights[0][0]
        for foglalas in self._bookedFlights:
            if foglalas[0] > max:
                max = foglalas[0]
        return max
