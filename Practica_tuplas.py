# Ejemplo de tupla
miTupla=("Juan", 13, 1, 1995)

# Imprimimos por consola el indice 2
print(miTupla[2])

# Insertamos los datos de una dupla dentro de una lista con la funcion list
miTupla=("Juan", 13, 1, 1995)
miLista=list(miTupla)

# Insertamos los datos de una lista dentro de una tupla con la funcion tuple
miLista=["Juan", 13, 1, 1995]
miTupla=tuple(miLista)

# Al igual que con las lista la funcion in nos permite buscar si hay un dato en una tupla
print("Juan" in miTupla)

# Con la funcion count nos devuelve el numero de veces que esta ese valor repetido en una tupla
print(miTupla.count(1))

# La funcion len lo que nos permite es saber cuandos elementos hay en una tupla
print(len(miTupla))

# Tupla unitaria, siempre con la coma despues de insertarle un dato
miTupla=("Juan",)
print(len(miTupla))

# Asignamos los valores de una tupla a las variables designadas
miTupla=("Juan", 13, 1, 1995)
nombre, dia, mes, agno=miTupla
print(nombre)
print(dia)
print(mes)
print(agno)
