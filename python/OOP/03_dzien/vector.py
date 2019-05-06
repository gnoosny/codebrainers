import math   

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, skalar):
        return Vector(self.x * skalar, self.y * skalar)
    def __truediv__(self, skalar):
        return Vector(self.x / skalar, self.y / skalar)
    def __str__(self):
        return "Vector({}, {})".format(self.x, self.y)
    def __abs__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))
    def __neg__(self):
        return Vector(-self.x, -self.y)



wekt1 = Vector(2, 3)
wekt2 = Vector(4, 1)

dodawanie = wekt1 + wekt2
odejmowanie = wekt1 - wekt2

mno_skal = wekt1 * 3
dziel_skal = wekt2 / 3



print("suma: ", dodawanie.x, dodawanie.y)
print("odejmowanie: ", odejmowanie.x, odejmowanie.y)
print("mnożenie: ", mno_skal.x, mno_skal.y)
print("dzielenie przez skalar: ", dziel_skal.x, dziel_skal.y)
print(str(wekt1))
print(abs(wekt1))
wekt1 = -wekt2
print(wekt1)
# print()
# print(neg(wekt1))