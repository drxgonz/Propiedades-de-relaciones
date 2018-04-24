#Este archivo contiene el algoritmo para comprobar la propiedad irreflexiva

#Nota: Considerando que si no hay que con que comparar se toma por valida...

def propiedadIrreflexiva(conjunto, relacion):
	
	#DEVOLVERÁ 1 SI CUMPLE, 0 SI NO.
	#Se da por hecho que todos los pares ordenados de la relacion pertenecen al conjunto (Ya se comprobo con validacionGeneral.py)
	
	pilaComparaciones = []
	#Esta lista booleana tiene como fin anadir 1 o 0 cada que se ejecute el ciclo for (linea 21), pues si hay algun 1, cumple la propiedad y se retorna 1
	listaAuxiliar = []
	#Esta lista tiene como fin almacenar los pares ordenados del tipo: (a,a)  que se generaran a partir de los elementos del conjunto y servira para buscar en los pares ordenados de la relacion
	
	for elemento in conjunto:
		listaAuxiliar.append([elemento,elemento])
		
	
	for parOrdenado in listaAuxiliar:
		if parOrdenado  not in relacion:
			pilaComparaciones.append(1) 
			#Cumple
		else:
			pilaComparaciones.append(0)
	
	if 0 not in pilaComparaciones:
		#cumple
		return 1
	else:
		return 0
		
#print(propiedadIrreflexiva([1,2,3,4],[[3,4]]))#Si es
#print(propiedadIrreflexiva([1,2,3,4],[[2,1],[3,1],[3,2],[4,1],[4,2],[4,3]])) #Si es
#print(propiedadIrreflexiva([1,2,3,4],[[1,1],[1,2],[2,1],[2,2],[3,4],[4,1],[4,4]])) #No es