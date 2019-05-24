class KontoBankowe:
    def __init__(self, nazwisko, stan=0):
        self.nazwisko = nazwisko
        self.stan = stan
 
    def info(self):
        print("Konto bankowe", self.nazwisko,
              "<stan:", self.stan, ">")
 
    def wplac(self, kwota):
        self.stan += kwota
 
    def wyplac(self, kwota):
        self.stan -= kwota
 
    def przelew(self, konto_docelowe, kwota):
        self.stan -= kwota
        konto_docelowe.stan += kwota
 
 
if __name__ == "__main__":
    jk = KontoBankowe("Jan Kowalski")
    jn = KontoBankowe("Janusz Nowak", 1000)
 
    jk.info()
    jn.info()
 
    jn.przelew(jk, 500)
 
    jk.info()
    jn.info()