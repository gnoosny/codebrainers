class NazwaKlasy:
    name = "Mars"
    price = 3.99
    def metoda(self):
        print(self.name)
        print(self.price)

obiekt = NazwaKlasy()

obiekt.metoda()


class KlasaDruga:
    def __init__(self, prod):
        self.name = "Snickers"
        self.price = 5.99
        self.product = prod
        print(self.name + " " + str(self.price) + " " + prod)

obiekt2 = KlasaDruga("baton")

obiekt2.price