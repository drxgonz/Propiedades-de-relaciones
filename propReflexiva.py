#Este archivo contiene el algoritmo para comprobar la propiedad reflexiva

#[PROBANDO CON UN CASO ESPECIFICO] Utilizando el ejemplo visto en clase...
#Conjunto A =(1,2,3)
#R = { (1,1) (1,2) (3,2) (2,3) (3,3) }


def  propiedadReflexiva (conjunto,relacion):
	#DEVOLVERÁ 1 SI CUMPLE, 0 SI NO.
	#Se da por hecho que todos los pares ordenados de la relacion pertenecen al conjunto (Ya se comprobo con validacionGeneral.py)
	
	pilaComparaciones = []
	#Esta lista booleana tiene como fin anadir 1 o 0 cada que se ejecute el ciclo for (linea 21), pues si hay algun 1, cumple la propiedad y se retorna 1
	listaAuxiliar = []
	#Esta lista tiene como fin almacenar los pares ordenados del tipo: (a,a)  que se generaran a partir de los elementos del conjunto y servira para buscar en los pares ordenados de la relacion
	
	for elemento in conjunto:
		listaAuxiliar.append([elemento,elemento])
		
	
	for parOrdenado in listaAuxiliar:
		if parOrdenado  in relacion:
			pilaComparaciones.append(1)
		else:
			pilaComparaciones.append(0)
	
	if 0 not in pilaComparaciones:
		return 1
	else:
		return 0
		

#print(propiedadReflexiva([1,2,3],[[1,1],[1,2],[3,2],[2,3],[3,3]]))


########Otra prueba :v

#print(propiedadReflexiva([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(propiedadReflexiva([1,2,3,4],[[1,1],[1,2],[2,1]]))
#print(propiedadReflexiva([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(propiedadReflexiva([1,2,3,4],[[1,1],[1,2],[2,1]]))
#print(propiedadReflexiva([1,2,3,4],[[1,1],[1,2],[1,3],[1,4],[2,3],[2,2],[2,4],[3,3],[3,4],[4,4]]))
