# Usamos la funcion print() para imprimir por consola
print("Estamos aprendiendo Python")
print("Estamos aprendiendo instrucciones basicas")
print("Poco a poco iremos avanzando")

# Asi se define una funcion, no hace falta cerrarla, solamente haciendole una sangria con el tabulador a su contenido
def mensaje():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones basicas")
    print("Poco a poco iremos avanzando")

# Asi llamamos a una funcion
mensaje()

# Asi se define una funcion con parametros
def suma(num1, num2):
    resultado=num1+num2
    return resultado

print(suma(5,7))
print(suma(2,3))
print(suma(35,358))

# Almacenamos en una variable el resultado de la funcion
almacena_resultado=suma(5,8)

print(almacena_resultado)