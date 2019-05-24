import random

class Tamagochi:
    def __init__(self, imie, prog_nudy, prog_glodu, malenie_nudy, malenie_glodu, poziom_nudy, poziom_glodu, slowa, szczescie):
        self.imie = imie
        self.prog_nudy = prog_nudy
        self.prog_glodu = prog_glodu
        self.malenie_nudy = malenie_nudy
        self.malenie_glodu = malenie_glodu
        self.poziom_nudy = poziom_nudy
        self.poziom_glodu = poziom_glodu
        self.slowa = slowa
        self.szczescie = szczescie

    def humor(self):

        if self.poziom_nudy >= self.prog_nudy:
            self.szczescie = True
            print("zmiana")
        elif self.poziom_glodu >= self.prog_glodu:
            self.szczescie = True
        else:
            self.szczescie = False
            print("brak zmiany")
        
    def __str__ (self):
        print(self.poziom_nudy, self.poziom_glodu)
        if self.szczescie == True:
            return "Tamagochi {} {} czuje się źle".format(self.imie)
        else:
            return "Tamagochi {} {} czuje się dobrze".format(self.imie)
        self.zegar()
    def zegar(self):
        self.poziom_glodu += 1
        self.poziom_nudy += 1
    def zmniejsz_glod(self):
        if self.poziom_glodu - self.malenie_glodu >= 0:
            self.poziom_glodu -= self.malenie_glodu
            print("poziom glodu: ", self.poziom_glodu)
    def zmniejsz_nude(self):
        if self.poziom_nudy - self.malenie_nudy >= 0:
            self.poziom_nudy -= self.malenie_nudy
            print("poziom nudy: ", self.poziom_nudy)
    def przywitaj(self):
        print("{} mówi {}".format(self.imie, random.choice(self.slowa)))
    def naucz_slowo(self):
       slowo = input("Podaj słowo którego chcesz nauczyć swojego zwierzaka: \n")
       self.slowa.append(slowo)
    def karm(self):
        self.zmniejsz_glod()

pikacz = Tamagochi("Pikacz", 8, 8, 1, 1, 10, 10,  ["czesc", "kocham cię", "jak się masz?"], False)

pikacz.humor()

print(str(pikacz))

pikacz.zmniejsz_glod()
pikacz.zmniejsz_glod()
pikacz.zmniejsz_glod()
pikacz.zmniejsz_nude()
pikacz.zmniejsz_nude()

pikacz.humor()
pikacz.humor()
print(str(pikacz))

pikacz.przywitaj()
pikacz.naucz_slowo()
pikacz.przywitaj()
pikacz.przywitaj()
pikacz.przywitaj()
pikacz.przywitaj()