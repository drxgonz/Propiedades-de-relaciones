#Este archivo contiene el algoritmo para comprobar la propiedad simetrica

#[PROBANDO CON UN CASO ESPECIFICO] Utilizando el ejemplo visto en clase...
#Conjunto A =(1,2,3,4)
#R = { (1,1) (1,2) (2,1) }

#Nota: Considerando que si no hay que con que comparar se toma por valida...

def propiedadSimetrica(conjunto, relacion):
	
	listaCoincidencias = []
	#Hace una funcion similar  a pilaComparaciones del algoritmo de la propiedad Reflexiva
	
	for  parOrdenado in relacion:
		a = parOrdenado[0]; b = parOrdenado[1]
		parAuxiliar = [b,a]
		if parAuxiliar not in relacion:
			listaCoincidencias.append(0)
		else:
			listaCoincidencias.append(1)
	
	if 0 not in listaCoincidencias:
		return 1
	else:
		return 0
		

#Pruebas		
#print(propiedadSimetrica([1,2,3],[[1,1],[1,2],[3,2],[2,3],[3,3]]))


########Otra prueba :v

#print(propiedadSimetrica([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(propiedadSimetrica([1,2,3,4],[[1,1],[1,2],[2,1]]))
#print(propiedadSimetrica([1,2,3,4],[[1,1],[1,2],[1,3],[1,4],[2,3],[2,2],[2,4],[3,3],[3,4],[4,4]]))