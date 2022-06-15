from merge_sort import *
from quick_sort import *
from shell_sort import *

def main():
	lista = [2,1]#[7,2,0,1,5,6,4,3,8,7]
	# print(selection(lista))
	# print(insertion(lista))
	# print(bubble(lista))
	# print(merge_sort(lista))
	# print(quick_sort(lista,0,len(lista)-1))
	print(shell_sort(lista))
    
def selection(lista):
	#para cada numero da lista
	for i in range(len(lista)-1):
		#selecione o menor e troque com a posicao i
		menor = i
		for j in range(i,len(lista)):
			if lista[j]<lista[menor]:
				menor = j
				#troca
				aux = lista[i]
				lista[i] = lista[menor]
				lista[menor] = aux
	return lista

def insertion(lista):
	#para cada elemento
	for i in range(1,len(lista)):
		#coloque o elemento na posicao correta
		j = i
		while lista[j]< lista[j-1] and j>0:
			aux = lista[j]
			lista[j] = lista[j-1]
			lista[j-1] = aux 
			j -=1
		return lista

def bubble(lista):
	for i in range(len(lista)-1):
		for j in range(len(lista)-1-i):
			if lista[j]>lista[j+1]:
				lista[j],lista[j+1]=lista[j+1],lista[j]
	return lista


main()

