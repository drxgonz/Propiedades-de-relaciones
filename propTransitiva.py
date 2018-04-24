#Este archivo contiene el algoritmo para comprobar la propiedad transitiva

#[PROBANDO CON UN CASO ESPECIFICO] Utilizando el ejemplo visto en clase...
#Conjunto A =(1,2,3,4)
#R = { (1,1) (1,2) (2,1) }

#Nota: Considerando que si no hay que con que comparar se toma por valida...

def propiedadTransitiva(conjunto, relacion):
	
	listaCoincidencias = []
	parAuxiliar = []
	
	
	for i in range(0, len(relacion)-1):
		parAuxiliarActual = [relacion[i][0],relacion[i][1]]
		parAuxiliarSiguiente = [relacion[i+1][0],relacion[i+1][1]]
		if parAuxiliarActual[1] == parAuxiliarSiguiente[0]:
			if parAuxiliar not in relacion:
				listaCoincidencias.append(0)
			else:
				listaCoincidencias.append(1)

	
	if 0 not in listaCoincidencias:
		return 1
	else:
		return 0

		
#print(propiedadTransitiva([1,2,3,4],[[2,1],[3,1],[3,2],[4,1],[4,2],[4,3]])) #Si es
#print(propiedadTransitiva([1,2,3,4],[[1,1],[1,2],[2,1],[1,4],[2,2],[3,4],[4,1],[4,4]])) #No es
