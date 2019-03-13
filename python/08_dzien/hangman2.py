# your code goes here
from random import randint

movies = ['The Godfather', 'Dark Knight', 'Pulp Fiction', 'Fight Club', 'Forrest Gump', 'Inception', 'Matrix']

rand = -1
rand = randint(0, 6)

password = movies[rand].lower()
password_list = password.split()
print(password_list)
first_word_len = len(password[0])
print(password[0])
space = 0
if len(password_list) == 1:
  password_list = list(password_list[0])
elif len(password_list) > 1:
  password_list = list(password_list[0]) + list(password_list[1])
  space = len(password_list[0])+1
  print(password_list[0])

password_len = len(password_list)

print(password_list, password_len)

if space == False:
  print("X" * password_len)
elif space:
  print("X" * space)
