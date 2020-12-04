print("Olá mundo")
print("Outra mensagem")
print("Okay")

# Comentário

"""
Comentários
muitas
linhas
"""
print("Acabou")

print(2+2)

variavel = "Olá world"

print(variavel)
print(variavel)
print(variavel)

var1 = 1
var2 = 1.1
var3 = "Eu sou foda"
var4 = False

print(var1)
print(var2)
print(var3)
print(var4)

y = 3
x = 2
soma = x + y

print(x == y)

print(x == y and x == soma)

print(x == y or x == soma)

if x > y:
	print("X é maior que Y")

if y > x:
	print("Y é maior que X")



if x > y:
	print("X maior que Y")
else:
	print("X não é maior que Y")

if x == y:
	print("Números iguais")
elif y > x:
	print("Y maior que X")
elif y < x:
	print("Y menor que X")

else:
	print("Números diferentes")

## Idade 

idade = 20

if idade >= 18:
    print("maior de idade")
elif idade < 18:
    print("menor de idade")
else:
    print("valor invalido")


x = 1 

while x < 10:
	print(x)
	x = x + 1


lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0,"ola","biscoito", "bolacha", 9.99, True]


for i in lista1:
	print(i)

for i in lista2:
	print(i)
for i in lista3:
	print(i)


## Números ímpares

i = 0

while i < 100:
    if(i%2 != 0):
         print(i)
    i+=1


for i in range(10,20,2):
	print(i)

numero = input("Digite um numero: ")
print("O numero digitado é:")
print(numero)

nome = input("Digite seu nome: ")
print("Bem vindo" +nome)


frutas = ["morango","uva","pera","tomate"]

frutas = ["morango","uva","pera","tomate"]
frutas.append("abacaxi")
for f in frutas:
    print(f)



#Strings

a = "Lucas"
b = "Fernandes"
ab = a + " " + b
print(ab)

tamanho = len(ab)
print(tamanho)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print (tamanho[0:7])

seq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print (seq)
print(seq.lower())
print(seq.upper())

seq = seq.lower()
print(seq)

seq = seq.upper()
print(seq)

sespaço = "LUCas \n Fernandes"

print(sespaço.strip())


minha_string = "O rato roeu a ropa do rei de Roma"

minha_lista = minha_string.split(" ")
print(minha_lista)


busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)



#Funções

def soma(a,b):
	return (a+b)

def multiplicacao(a,b):
	return x*y

 s = soma(34,23)
 m = multiplicacao (3,4)

print(soma(s,m))

#Arquivos

arquivo = open ("arquivo.txt")
linhas = arquivo.readlines()
print(linhas)

for linha in linhas
	print (linha)

texto = arquivo.read()

print(texto)


w = open("arquivo2.txt", "w")

w.write("Esse é o meu arquivo")

w.close()

w = open("arquivo.txt", "a")

w.write("\nEsse é o meu arquivo")

w.close()



#Listas

minha_lista = ["abacaxi", "melancia", "abacate", "maçã"]
print(minha_lista)

minha_lista2 = [1,2,3,4,5,6,7]
minha_lista3 = ["abacate", 2, 9.89, True]
minha_lista4 = []
print(minha_lista[2])

for item in minha_lista:
	print(item)
	
tamanho = len(minha_lista)

print(tamanho)

minha_lista.append("limão")

print(minha_lista)

if  7 in minha_lista2:
	print("7 está na lista")

del minha_lista[2:]
print(minha_lista)

del minha_lista[:]


minha_lista4.append(57)
print(minha_lista4)


lista = [5656,6565,323,12,12,12312,3232,,323,15,15154,6,46,4646,46546546]

lista.sort()
lista.sort(reverse = True)
lista.reverse()


print(lista)

lista = sorted(lista)
print(lista)


#Dicionários

meu_dicionario = {"A":"AMEIXA", "B" : "BOLA", "C":"CACHORRO"}
print(meu_dicionario)
print(meu_dicionario["A"])

for chave in meu_dicionario:
	print(chave)+": " + meu_dicionario)

for i in meu_dicionario.items():
	print(i)

for i in meu_dicionario.keys():
	print(i)

#Aleatorio 

import random

numero = random.randint(0,10)
print(numero)

lista = [2,4,65,232,23]

numero = random.choice(lista)


#Exceçoes

a = 2 
b = 0

try:
	print(a/b)

except: 
	print("Não é permitida divisão por 0")

print(a/a)


#list comprehension

x = [1,2,3,4,5]
y = [i**2 for i in x]
z = [i for i in x if i%2!=0]

print(x)
print(y)
print(z)

#Função Enumerate

lista = ["abacate", "bola", "cachorro"]

for i, nome in enumerate(lista):
	print(i, nome)

#map

def dobro(x):
	return x*2

valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor)

for v in valor_dobrado:
	print(v)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)


#reduce
from functool import reduce
def soma (x,y):
	return x+y

lista = [1,23,54,3,435,353,63,54,34,3,323]

soma = reduce(soma, lista)

print(soma)


#zip

lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro","elefante"]
lista3 = ["R$ 2,00","R$ 5,00","R$ 21,00","R$ 32,00","R$ 552,00"]


for numero, nome, valor in zip(lista1, lista2, lista3):
	print(numero, nome, valor)