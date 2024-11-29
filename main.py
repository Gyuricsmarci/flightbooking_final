from typing import final
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from Legitarsasag import Legitarsasag
from JegyFoglalas import JegyFoglalas
from datetime import datetime
from datetime import date

class bookingClass:
    def __init__(self):
        self._airLine = Legitarsasag("ZooWay Airlines")
        self.booking = JegyFoglalas(self._airLine)
        self.initData()

    def initData(self):
        global hiba
        hiba = False
        global mostido
        try:
            mostido = datetime.strptime(input("Kérem adja meg a jelenelegi dátumot ÉÉÉÉ.HH.NN. formában: \t"), "%Y.%m.%d.").date()
        except:
            print("Hibás dátum fordátum: (ÉÉÉÉ.HH.NN.)")
            hiba = True
            
        self._airLine.scheduledFlights = BelfoldiJarat("SKW-315", "egyéni", 3, "Budapest", "Debrecen", 50000, datetime.strptime("2024.12.30.", "%Y.%m.%d.").date())
        self._airLine.scheduledFlights = NemzetkoziJarat("SKW-999", "charter", 300,"Budapest", "New York", 129990, datetime.strptime("2025.12.10.", "%Y.%m.%d.").date())
        self._airLine.scheduledFlights = NemzetkoziJarat("SKW-651", "menetrendszerinti", 511,"Budapest", "Miami", 465990, datetime.strptime("2024.11.25.", "%Y.%m.%d.").date())
        self.booking.initBookAFlight(1, self._airLine.getScheduledFlight(0))
        self.booking.initBookAFlight(2, self._airLine.getScheduledFlight(1))
        self.booking.initBookAFlight(3, self._airLine.getScheduledFlight(2))
        self.booking.initBookAFlight(4, self._airLine.getScheduledFlight(0))
        self.booking.initBookAFlight(5, self._airLine.getScheduledFlight(1))
        self.booking.initBookAFlight(6, self._airLine.getScheduledFlight(1))
    def userInteract(self):
        try:
            while True and not hiba:
                lastId = self.booking.maxID() + 1
                print("1. Foglalások listázás")
                print("2. Jegy foglalás")
                print("3. Jegyfoglalás lemondása")
                print("4. Kilépés")
                
                choice = int(input("Kérem a funkciót: "))
                if choice == 1:
                    self.booking.bookedFlights
                elif choice == 2:
                    chosenNumber = input("Kérem adja meg a foglalandó járat számát: ")
                    index = 0
                    volteJarat = False
                    while index < len(self._airLine._scheduledFlights):
                        if chosenNumber == self._airLine.getScheduledFlight(index).flightNumber:
                            volteJarat = True
                            self.booking.bookAFlight(lastId, self._airLine.getScheduledFlight(index), mostido)
                        index = index + 1
                    if not volteJarat:
                        print("Nincs ilyen járat!")
                        
                elif choice == 3:
                    chosenNumber = int(input("Kérem adja meg a törölni kívánt foglalás azonosítóját: "))
                    self.booking.cancelAFlight(chosenNumber)
                    
                elif choice == 4:
                    break
                elif choice > 4 or choice <= 0:
                    print("Nincs ilyen funkció!")
            
        except ValueError:
            print("A megadott adat hibás!")
    
bs = bookingClass()
bs.userInteract()