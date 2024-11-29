class Legitarsasag:
    def __init__(self, airlineName):
        self._airlineName = airlineName
        self._scheduledFlights = []

    @property
    def airlineName(self):
        return self._airlineName

    @property
    def scheduledFlights(self):
        for jarat in self._scheduledFlights:
            print(f"{jarat.flightNumber} számú járat {jarat.flightOrigin} -ból/ből, {jarat.flightDestination} -ba/be, egy {jarat.flightType} járat. Az ára: {jarat.flightPrice}")

    def getScheduledFlight(self, i):
        return self._scheduledFlights[i]

    @scheduledFlights.setter
    def scheduledFlights(self, newFlight):
        self._scheduledFlights.append(newFlight)

    def getContentOfScheduledFlights(self):
        return self._scheduledFlights

    def __len__ (self):
        return len(self._scheduledFlights)
    
