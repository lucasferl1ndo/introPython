minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5,6,7,8,9,10]
minha_lista3 = ["abacaxi", 2, 21.21,True]
 minha_lista4 = []

print(minha_lista[1])

for item in minha_lista:
	print(item)

tamanho = len(minha_lista)
print(tamanho)

minha_lista.append("limão")


print(minha_lista)

if 7 in minha_lista2:
	print(" 7 está na lista 2")

del minha_lista[2:]
print(minha_lista)

minha_lista4.append(57)
print(minha_lista4)


lista = [121,3,4,212,543,546543,43232,23,4556,6]
lista.sort()
lista.sort(reverse=True)
lista.reverse()
print(lista)

lista = sorted(lista)
print(lista)


lista2 = ["bola", "abacate", "dinheiro", "rato"]
lista.sort()
pritn(lista2)