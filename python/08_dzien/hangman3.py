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

def search(letter, hash):
  #for number, letter in enumerate(password):
    hash_new = hash
    if letter in password:
      print("yes")
      print(password.index(letter))
      print(hash_new[0:password.index(letter)] + letter + hash_new[password.index(letter):password_len])
      hash_new = hash_new[0:password.index(letter)] + letter + hash_new[password.index(letter):password_len]
      letter = input("enter a letter: ")
      search(letter, hash_new)
    else:
      print("no")
      search(letter, hash_new)
