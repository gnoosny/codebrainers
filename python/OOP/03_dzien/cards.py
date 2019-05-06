from random import shuffle

class Card:
    def __init__(self, num, col):
        self.num = num
        self.col = col
    def __str__(self):
        return "Karta <{} {}>".format(self.num, self.col)

class Deck():
    def __init__(self):
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        colors = ['pik', 'kier', 'trefl', 'karo']
        # for i in value:
        #     for y in colors:
        #         self.stos.append(Card{[i],[y]})

        self.stos =[Card(num, col)for col in colors for num in value] 
        shuffle(self.stos)

    def __iter__(self):
        return iter(self.stos)

   
    
talia = Deck()

for i in talia:
    print(i)
