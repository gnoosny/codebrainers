# szesciany = []

# for x in range(1,101):
#     szesciany.append(x ** 3)

# print(szesciany)

# szesciany = [x**3 for x in range(1,101)]

# print(szesciany)

sq = [x ** 2 for x in range(1, 101) if x % 5 == 0 and x % 9 == 0]

print(sq)
