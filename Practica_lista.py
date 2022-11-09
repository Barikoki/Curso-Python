# Listas
# ------
# Asi se crea una lista
miLista=["Maria","Pepe","Marta","Antonio"]

# Asi imprimimos por pantalla todo el contenido de la lista
print(miLista[:])

# Asi imprimimos el contenido de un indice concreto
print(miLista[1])

# Si ponemos un indice negativa lo empieza a contar desde el final a la izquierda, empezando siempre por el -1, no por el 0
print(miLista[-2])

# Porciones de lista
# ------------------
# Imprimimos una porcion desde el 0 inclusive y el 3 exclusive, asi que imprimiria solo los indices 0, 1 y 2
print(miLista[0:3])

# Esto es equivalente al ejemplo anterior, iria desde el primer indice hasta el 2, el 3 queda fuera
print(miLista[:3])

# Esto imprimiria solo el indice 1
print(miLista[1:2])

# Esto imprimiria desde el indice 2 hasta el final
print(miLista[2:])

# Insertar datos en lista
# -----------------------
# Insertamos un dato al final de la lista
miLista.append("Sandra")

# Insertamos un dato en el indice que le indiquemos
miLista.insert(2,"Manuel")

# Insertamos varios elementos a la lista
miLista.extend(["Vero", "Ana", "Lucia"])

# Con esta funcion indicamos que nos indique el indice donde esta el dato que pongamos
print(miLista.index("Vero"))

# Con esta funcion imprimimos por consola si un dato esta en una lista devolviendo True y False en el caso de que no este en la lista
print("Pepe" in miLista)

# Listas con diferentes tipos de dato
miLista=["Maria",5, True, 78.35]
miLista.extend(["Sandra", "Ana", "Lucia"])

# Eliminar datos en lista
# -----------------------
# Asi eliminamos un dato de una lista
miLista.remove("Ana")

# Asi eliminamos el ultimo dato de un lista
miLista.pop()

# Concatenamos 2 listas en una
miLista=["Maria", 5, True, 78.35]
miLista2=["Sandra", "Lucia"]
miLista3=miLista+miLista2

# Con el operador * multiplicamos el numero de veces una lista
miLista=["Maria", 5, True, 78.35] * 3