# Ejercicio 1
# Crea un programa que pida números infinitamente. Los números introducidos deben ser 
# cada vez mayores El programa finalizará cuando se introduce un número menor que el anterior.
numero=int(input("Por favor, introduce un numero\n"))
numero_ant=-1

while numero>numero_ant:
    numero_ant=numero
    numero=int(input("Por favor, introduce un numero mayor que " + str(numero) + "\n"))

print("El numero insertado no es mayor que el anterior, hasta siempre!")

# Ejercicio 2
# Crea un programa que pida números positivos indefinidamente. El programa termina cuando se 
# introduce un número negativo. Finalmente el programa muestras la suma de todos los números 
# introducidos.
num=int(input("Por favor, introduzca un numero positivo\n"))
total=0

while num>=0:
    total+=num
    num=int(input("Por favor, introduzca otro numero positivo\n"))
print("El numero es negativo. La suma total de todos los numeros es: " + str(total))