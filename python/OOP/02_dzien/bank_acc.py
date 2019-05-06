class BankAccount:
    def __init__(self, name, state=0):
        self.name = name
        self.state = state
        self.hist = []
    def info (self):
        print("Imie i nazwisko: ", self.name)
        print("Stan rachunku: ", self.state)
        print("\n")
    def take_out(self, quantity):
        self.state -= quantity
    def deposit(self, quantity):
        self.state += quantity
    def transfer(self, account_number, quantity):
        self.state -= quantity
    def history_add(self, move, quantity):
        self.hist.append([move, quantity])
    def history(self):
        if not self.hist:
            print("Brak historii rachunku\n")
        else:
            for i in range(0, len(self.hist)):
                print("Rodzaj operacji: " + self.hist[i][0] + "\nKwota: " + str(self.hist[i][1]))
    

jk = BankAccount("Jan Kowalski", 1000)
pn = BankAccount("Piotr Nowak",)

operation = 0

def clear_screen():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def operacja():
    print("Co chcesz zrobic?\n1. Pokaz informacje o rachunku\n2. Wplac gotowke\n3. Wyplac gotowke\n4. Wykonaj przelew\n5. Pokaz historie operacji\n6. Zakoncz operacje\n")
    operation = input("Wybierz liczbe: ")
    clear_screen()
    if operation is "1":
        jk.info()
        operacja()
    elif operation is "2":
        print("Jaka sume chcesz wplacic?")
        dep = int(input())
        jk.deposit(dep)
        jk.history_add("Wplata", dep)
        print("\n")
        jk.info()
        operacja()
    elif operation is "3":
        print("Jaka sume chcesz wyplacic?")
        take_o = int(input())
        if jk.state - take_o >=0:
            jk.take_out(take_o)
            jk.history_add("Wyplata", take_o)
            print("\n")
            jk.info()
        else:
            print("Brak wystarczajacych srodkow na koncie\n")
        operacja()
    elif operation is "4":
        print("Podaj numer rachunku na ktory ma trafic przelew")
        acc_n = input()
        if len(acc_n) != 10:
            print("Numer konta jest nieprawidlowy\n")
            operacja()
        acc_n = int(acc_n)
        print("Jaka sume chcesz wyslac?")
        trans = int(input())
        if jk.state - trans >= 0:
            jk.transfer(acc_n, trans)
            jk.history_add("Przelew na rachunek: " + str(acc_n), trans)
            print("\n")
            jk.info()
        else:
            print("Brak wystarczajacych srodkow na koncie\n")
        operacja()
    elif operation is "5":
        jk.history()
        print("\n")
        operacja()
    elif operation is "6":
        print("Koniec operacji.\nMilego dnia")
    else: 
        print("Wybrano nieprawidlowe polecenie. Wybierz jeszcze raz")
        operacja()
clear_screen()
operacja()

