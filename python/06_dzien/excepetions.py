try:
	1/0
except ZeroDivisionError:
	print("nie dziel przez zero")

lista = [1, 2, 3]

try:
	lista[123]
except IndexError:
	print("Element listy nie istnieje")

slownik = {"key": "1"}

try:
	slownik['nie istniejsacy klucz]']
except KeyError:
	print("klucz nie istnieje")

try:
	lista.funkcja()
except AttributeError:
	print("atrybut nie istnieje")

try:
	nie_istnieje()
except NameError:
	print("funkcja nie istnieje")

class MojaKlasa:
    zmienna = "blah"

obiekt = MojaKlasa()

try:
	obiekt.zmienna()
except TypeError:
	print("obiekt nie posiada tego atrybutu")

try:
	"b" = "a"
except SyntaxError:
	print("blad skladni")

