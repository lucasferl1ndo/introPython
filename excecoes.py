import random

a = 2
b = 0

try:
	print(a/b)
except:
	print("Não é permitida divisão por 0")

print(a/a)
lista = [5,6,23,23]

numero = random.randint(0,1000)

numero = random.choice(lista)

print(numero)