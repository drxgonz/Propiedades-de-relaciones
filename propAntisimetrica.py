#Este archivo contiene el algoritmo para comprobar la propiedad antisimetrica

#Nota: Considerando que si no hay que con que comparar se toma por valida...

def propiedadAntisimetrica(conjunto, relacion):
	
	listaCoincidencias = []
	#Hace una funcion similar  a pilaComparaciones del algoritmo de la propiedad Reflexiva
	
	for  parOrdenado in relacion:
		a = parOrdenado[0]; b = parOrdenado[1]
		parAuxiliar = [b,a]
		if parAuxiliar not in relacion:
			#Pues si existe (1,3) y (3,1), a es diferente de b, por lo tanto ya no cumpliria
			listaCoincidencias.append(1)
		else:
			listaCoincidencias.append(0)
	
	if 0 not in listaCoincidencias:
		return 1
	else:
		return 0

#print(propiedadAntisimetrica([1,2,3,4],[[3,4]]))#Si es
#print(propiedadAntisimetrica([1,2,3,4],[[1,1],[1,2],[2,1],[2,2],[3,4],[4,1],[4,4]])) #No es
#print(propiedadAntisimetrica([1,2,3,4],[[1,1],[1,2],[1,3],[1,4],[2,3],[2,2],[2,4],[3,3],[3,4],[4,4]])) #si es
