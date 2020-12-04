arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

for linhas in linhas:
	print(linhas)

texto = arquivo.read()
print(texto)


w = open("arquivo.2.txt", "w")

w.write("Esse é o meu arquivo\n")
w.close()