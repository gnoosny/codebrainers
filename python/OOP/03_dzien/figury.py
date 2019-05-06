import math


class Figura:
    def obwod(self):
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):
        """Obliczanie pola powierzchni."""
        raise NotImplementedError

class Circle(Figura):
    def __init__(self, r):
        self.r = r
    def obwod(self):
        return 2 * math.pi * self.r
    def pole(self):
        return (self.r ** 2) * math.pi

class Triangle(Figura):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def obwod(self):
        return self.a + self.b + self.c
    def pole(self):
        return (self.a * self.h)/2

class Square(Figura):
    def __init__(self, a):
        self.a = a
    def obwod(self):
        return self.a * 4
    def pole(self):
        return pow(self.a, 2)

class Rectangle(Square):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    def obwod(self):
        return 2 * self.a + 2 * self.b
    def pole(self):
        return self.a * self.b

class Parallelogram(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h
    def pole(self):
        return self.a * self.h

class Trapeze(Parallelogram):
    def __init__(self, a, b, h, d):
        super().__init__(a, b, h)
        self.d = d
    def obwod(self):
        return self.a + self.b + self.h + self.d
    def pole(self):
        return ((self.a + self.b) / 2) * self.h