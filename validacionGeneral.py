#Este apartado tiene como finalidad  verificar que los pares ordenados de cada relacion pertenezcan al conjunto +

#[PROBANDO CON UN CASO ESPECIFICO] Utilizando el ejemplo visto en clase...
#Conjunto A =(1,2,3)
#R = { (1,1) (1,2) (3,2) (2,3) (3,3) }


def pertenenciaAlConjunto(conjunto, relacion):
	#Conjunto y relacion son listas
	#DEVOLVERÁ 1 SI CUMPLE, 0 SI NO.
	for parOrdenado in relacion:
		for elemento in conjunto:
			if parOrdenado[0] not in conjunto or parOrdenado[1] not in conjunto:
				return 0
	return 1
				
				
				
#print(pertenenciaAlConjunto([1,2,3],[[1,2],[1,2],[3,3],[2,3],[3,3]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[2,1]]))	


#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[2,1]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[1,4],[2,1],[2,2],[3,3],[4,1],[4,4]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[2,1]]))
#print(pertenenciaAlConjunto([1,2,3,4],[[1,1],[1,2],[1,3],[1,4],[2,3],[2,2],[2,4],[3,3],[3,4],[4,4]]))


#Pd. Si funciono :v 
