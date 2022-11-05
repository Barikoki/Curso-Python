# Ejemplo de diccionario en Python con sus claves y valores. Alemania es la clave y el valor es Berlin
miDiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
print(miDiccionario)

# Asi se imprime el valor de una clave de un diccionario
print(miDiccionario["España"])

# Asi se agregan mas elementos a un diccionario
miDiccionario["Italia"]="Roma"

# Asi se modifica un elemento de un diccionario
miDiccionario["Italia"]="Ciudad de Roma"

# Asi se elimina un elemento de un diccionario
del miDiccionario["Reino Unido"]

# Ejemplo de diccionario con claves con varios tipos de dato
miDiccionario={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}

# Asiganmos los valores a una tupla como claves de un diccionario
miTupla=["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario={miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlin"}

# Creamos una tupla dentro de un valor de un diccionario
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario["anillos"])

# Creamos un diccionario dentro de otro diccionario
miDiccionario={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario["anillos"])

# Imprimimos por pantalla todas las keys de un diccionario
print(miDiccionario.keys())

# Imprimimos por pantalla todos los valores de un diccionario
print(miDiccionario.values())

# Imprimimos por pantalla el numero de elementos que tiene el diccionario
print(len(miDiccionario))