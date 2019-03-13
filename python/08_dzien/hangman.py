#print("  ____\n |	  |\n |    O\n |	 -+-\n |	  |\n |   / \\\n/ \\")
from random import randint
import re
from re import match

movies = ['The Godfather', 'Dark Knight', 'Pulp Fiction', 'Fight Club', 'Forrest Gump', 'Inception', 'Matrix']
rand = -1
rand = randint(0,6)
#regex = "(g\w+)"
#regex = "/[a-z]/g"
regex = "\w"
password = movies[rand].lower().replace(regex, "X")
password = password.replace("\w", "")

print(password)

password2 = "XXXX XXXXX"
true_password = 'Dark Knight'

"""letter = ""
for i in range(10):
  letter = input("enter a letter: ")
  if true_password.lower().match(letter):
    print("match!")"""
