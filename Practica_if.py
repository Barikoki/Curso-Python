# Ejemplo de introduccion de datos por consola
print("Programa de evalucion de notas de alumnos")
nota_alumno=input("Introduce la nota del alumno")

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))