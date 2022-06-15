def shell_sort(lista):
	h = 1
	while h<len(lista):
		h = 3*h+1
	print('h: ',h)
	while h!=1:
		h = h//3
		print('h: ',h)
		for i in range(h,len(lista)):
			aux = lista[i]
			j = i
			while lista[j-h]>aux:
				lista[j] = lista[j-h]
				j-=h
				if j<h:
					break
			lista[j] = aux
	return lista	