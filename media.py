from statistics import *




def media(lista):
	#media = mean(lista)
	media = sum(lista)/float(len(lista))
	return media


def mediana(lista):
	#mediana = median(lista)
	lista_ordenada = sorted(lista)
	t = len(lista_ordenada)

	if tam % 2 == 0:

		mediana = (lista_ordenada[int(t/2)] + lista_ordenada[int((t/2)-1)]) / 2
	elif t % 2 == 1:
		mediana = lista_ordenada[int((t/2))]

	return mediana

def moda(lista):
	#moda = mode(lista)

	moda_dic = {}

	for l in lista:
		if l not in moda_dic:
			moda_dic[l] = 1
		else:
			moda_dic[l] += 1

	maior_repeticao = max(moda_dic.values())

	for i in moda_dic:
		if moda_dic[i] == maior_repeticao:
			moda = i
	return moda


