# Ejemplo sin usar generadores
def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista
print(generaPares(10))

# Ejemplo de Generador en Python
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)

# Otro ejemplo de generador en Python
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares(10)

print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))
print("Aqui podria ir mas codigo...")
print(next(devuelvePares))

# Ejemplo de for anidado sin usar la funcion yield from
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento:
            yield subelemento

ciudades_devueltas=devuelve_ciudades("Madrid"," Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

# Como el ejemplo anterior pero usando la funcion yield from
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid"," Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))