class CiagArytmetyczny:
    def __init__(self, a0, r):
        self.a0 = a0
        self.r = r

    def __iter__(self):
        return self

    def __next__(self):
        self.a0 += self.r
        if self.a0 > 100:
            raise StopIteration
        return self.a0


cg = CiagArytmetyczny(10, 3)

for i in cg:
    print(i)