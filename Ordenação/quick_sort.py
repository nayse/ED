def quick_sort(lista,p,r):
	if p<r:
		q = particao(lista,p,r)
		quick_sort(lista,p,q)
		quick_sort(lista,q+1,r)
	return lista

def particao(lista,p,r):
	pivo = lista[(p+r)//2]
	i = p-1
	j = r+1
	while i < j:
		j-=1
		while lista[j]>pivo:
			j-=1
		i +=1
		while lista[i]<pivo:
			i+=1
		if i<j:
			lista[i],lista[j] = lista[j],lista[i]
	return j
