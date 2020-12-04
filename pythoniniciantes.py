"""Python para iniciantes"""


valorhora = 4
dias = 30
horastrabalho = 8

salario = (valorhora * horastrabalho) * dias
nome = "Lucas"

print(nome)

print( salario)

lista = [1,4,5,6,"lucas"]

print(lista)
lista.append("Python")


lista.index("lucas")

lista.count(4)


lista.remove(4)

print(lista)

lista.reverse()
print(lista)

lista2 = [1,4,5,6,7,45,12]
lista2.sort()
print(lista2)



telefones = {"Lucas" : 1959565656, "Laura" : 65656565656, "Pedro" : 5656565656}
telefones["rita"] = 9595656
print(telefones)

del telefones ["Pedro"]


tuplas = ("tiago", "Python", "udemy")
print(tuplas)

print(tuplas[2])

len(tuplas)
