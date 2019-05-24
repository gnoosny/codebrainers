import bank

class KontoDebetowe(bank.KontoBankowe):
    def __init__(self, nazwisko, stan=0, limit=0):
        # bank.KontoBankowe.__init__(self, nazwisko, stan)
        # to jest to samo co nizej
        super().__init__(nazwisko, stan)
        self.limit = limit
    
    def wyplac(self, kwota):
        if self.stan - kwota < -self.limit:
            print("Operacja niedozwolona: limit na koncie")
        else:
            super().wyplac(kwota)
    def przelew(self, konto_docelowe, kwota):
        if self.stan - kwota < -self.limit:
            print("Operacja niedozwolona: limit na koncie")
        else:
            super().przelew(konto_docelowe, kwota)
    


pl = KontoDebetowe("Przemek Leksa", 1000000, 100000)
en = KontoDebetowe("Edward Nóżka")

pl.info()
pl.wplac(200)
pl.info()
pl.wyplac(300)
pl.info()
en.info()
pl.przelew(en, 5000)
pl.info()
en.info()

pl.przelew(en, 1100000)
pl.info()
en.info()

pl.przelew(en, 22000)
pl.info()
en.info()