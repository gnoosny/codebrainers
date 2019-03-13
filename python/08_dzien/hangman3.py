# your code goes here
from random import randint

movies = ['The Godfather', 'Dark Knight', 'Pulp Fiction', 'Fight Club', 'Forrest Gump', 'Inception', 'Matrix']

rand = -1
rand = randint(0, 6)

space = movies[rand].find(" ")
title = movies[rand]
print(title)
print("Space at: ", space)

password = title.lower()

print("psw: " + password)

password_len = len(password)
print(password_len)
hash = ""

if space < 0:
  hash = "X" * password_len
  print(hash)
elif space > 0:
  hash = "X" * space + " " + "X" * (password_len - space - 1)
  print(hash)

letter = input("enter a letter: ")

def search(letter):
  #for number, letter in enumerate(password):
    if letter in password:
      print("yes")
      print(password.index(letter))
      print(hash[0:password.index(letter)] + letter)
    else:
      print("no")

print(search(letter))
