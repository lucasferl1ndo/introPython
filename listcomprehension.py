# list comprehension

x = [1,2,3,4,5]
y = [i**2 for i in x ]
z = [i for i in x if i%2 == 1 ]

print("Usando list comprehension")
print(x)
print(y)
print(z)


# enumerate

lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
	print(i, nome)


# filter
def pares(i):
	if i % 2 == 0:
		return i


lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares,lista)
print(list(lista_pares))



# reduce
from functools import reduce
def soma(x,y):
	return x+y

lista = [1,3,5,10,20]

soma = reduce(soma,lista)
print(soma)

#map

def dobro(x):
	return x*2

valor = [1,2,3,4,5]
valor_dobrado = map(dobro,valor)

for v in valor_dobrado:
	print(v)


valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

#lambda

valor = [1,2,3,4,5]
valor_dobrado = map(lambda i: i*2,valor)


valor_dobrado = list(valor_dobrado)
print(valor_dobrado)


#zip

lista1 = [1,2,3,4,5]
lista2 = ["Abacate", "Banana", "Cereja", "Damasco", "Figo"]
lista3 = ["R$ 2,00","R$ 4,00","R$ 6,00","R$ 13,00","R$ 5,00"]

for numero, nome in zip(lista1,lista2, lista3):
	print(numero, nome, valor)