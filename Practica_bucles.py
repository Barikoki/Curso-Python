# Ejemplo de bucle for imprimiendo "Hola" tantas veces como elementos tiene la lista del ejemplo
for i in [1,2,3]:
    print("Hola")

# Ejemplo de bucle for recorriendo e imprimiendo los elementos de la lista del ejemplo
for estaciones in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(estaciones)

# Usamos la funcion end para imprimir por pantalla en una sola linea y dividido por los caracteres que le pongamos en el end
for i in["Pildoras", "Informaticas", 3]:
    print("Hola", end=" - ")

# Recorremos con el for todos los caracteres del String y nos imprime Hola tantas veces como caracteres tenga, separados por un espacio
for i in "juan@pildorasinformaticas.es":
    print("Hola", end=" ")

# Comprobamos caracter a caracter si el String tiene una arroba e imprimimos por pantalla el mensaje correspondiente
miEmail=input("introduce tu direccion de email: ")
email=False
for i in miEmail:
    if(i=="@"):
        email=True

if email:
    print("Email correcto")
else:
    print("Email no es correcto")

# Otro ejemplo de recorrido de email
contador=0
miEmail=input("introduce tu direccion de email: ")

for i in miEmail:
    if(i=="@" or i=='.'):
        contador=contador+1

if contador==2:
    print("Email correcto")
else:
    print("Email no es correcto")

# Crea como un array del numero de elementos que le indiquemos y lo muestra por pantalla
for i in range(5):
    print(i)

# Gracias a la f antes del String a impirmir, se puede formatear la salida para unir diferentes tipos de datos
for i in range(5):
    print(f"Valor de la variable {i}")
    print("Valor de la variable " + str(i))

# Recorre del 5 al 9, ya que el ultimo numero no es inclusivo
for i in range(5,10):
    print(f"Valor de la variable {i}")

# El tercer valor en el range no indica que tiene que recorrer del 1 al 49 pero de 3 en 3. Empezaria 1, 4, 7, 10...
for i in range (1,50,3):
    print(i)

# Otra forma de recorrer el email
valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")