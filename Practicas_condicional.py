# Ejemplo 1
# ---------
edad=17
# Ejemplo de if con varios operadores en el condicional
if  0<edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")

# Ejemplo 2
# ---------
# Para concatenar String con numeros, primero hay que castear los numeros a String
salario_presidente=int(input("Introduce salario Presidente"))
print("Salarios Presidente " + str(salario_presidente))

salario_director=int(input("Introduce salario Director"))
print("Salarios Director " + str(salario_director))

salario_jefearea=int(input("Introduce salario Jefe Area"))
print("Salarios Jefe Area " + str(salario_jefearea))

salario_administrativo=int(input("Introduce salario Administrativo"))
print("Salarios Administrativo " + str(salario_administrativo))

if salario_presidente>salario_director>salario_jefearea>salario_administrativo:
    print("Los salarios estan correctos")
else:
    print("Los salarios estan incorrectos")
# Ejemplo 3
# ---------
print("Programa de becas año 2022")

distancia_escuela=int(input("Introduce la distancia a la escuela en Kilometros\n"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro\n"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto\n"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

# Ejemplo 4
# ---------
print("Aisgnaturas optativas año 2022")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")
