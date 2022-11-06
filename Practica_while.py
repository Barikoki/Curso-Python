import math
# Ejemplo de bucle while
i=1
while i<=10:
    print("Ejecucion " + str(i))
    i+=1
print("Termino la ejecucion")

# Otro ejemplo de bucle while
edad=int(input("Por favor, introduzca la edad"))
while edad<0 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a interntarlo")
    edad=int(input("Por favor, introduzca la edad"))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante: " + str(edad))

#
print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0
while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos, el programa ha finalizado")
        break;

    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos+=1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))
