class A:
    """Rodzic pierwszy"""

    def __init__(self):
        super().__init__()
        self.a = "A"

    def f(self):
        print("a:", self.a)


class B:
    """Rodzic drugi"""

    def __init__(self):
        super().__init__()
        self.b = "B"

    def f(self):
        print("b:", self.b)


class Pochodna(A, B):
    """Dziecko"""

    def __init__(self):
        super().__init__()

