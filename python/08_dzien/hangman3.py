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
password_change = password

print("psw: " + password)

password_len = len(password)
print(password_len)
hash = ""

if space < 0:
  hash = "#" * password_len
  print(hash)
elif space > 0:
  hash = "#" * space + " " + "#" * (password_len - space - 1)
  print(hash)

letter = input("enter a letter: ")

def search(letter, hash):
  #for number, letter in enumerate(password):
    hash_new = hash
    if letter in password_change:
      print("\nI've guesed the letter!")
      print(password_change.index(letter))
      
      hash_new = list(hash_new)
      hash_new[password_change.index(letter)] = letter
      hash_new = "".join(hash_new)

      print(hash_new)
      if hash_new == password:
        print("Congratulations you've won!")
      letter = input("enter a letter: ")
      search(letter, hash_new)
    else:
      print("\nThere is no " + letter + " in the password")
      letter = input("enter a letter: ")
      search(letter, hash_new)
print(search(letter, hash))
