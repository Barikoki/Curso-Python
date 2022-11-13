# Ejemplos de manipulacion de cadenas
texto="   Hola que tal? Estamos aprendiendo Python!"
print(texto) # Imprime el texto anterior
print(texto.upper()) # Imprime el texto y lo pone todo en mayusculas.
print(texto.lower()) # Imprime el texto y lo pone todo en minusculas.
print(texto.capitalize()) # Imprime el texto y te pone la primera letra en mayuscula.
print(texto.count("a")) # Imprime el numero de veces que sale un caracter o grupo de caracteres en un texto.
print(texto.find("t")) # Imprime la posicion de un caracter o grupo de caracteres en un texto.
print(texto.isdigit()) # Imprime si el texto es un valor numerico.
print(texto.isalnum()) # Imprime si el texto contiene letras y numeros. No aceptea ni espacios ni caracteres.
print(texto.isalpha()) # imprime si el texto contiene solo letras. Ni numeros, espacios o caracteres.
print(texto.split()) # Imprime una lista de todas las palabras del texto separadas por espacios.
print(texto.strip()) # Imprime el texto eliminando los espacios que pueda tener al principio y a final de linea.
print(texto.replace("a", "e")) # Imprime el texto pero reemplazando un caracter o grupo de caracteres por otros.
print(texto.rfind()) # Imprime la posicion de un caracter o grupo de caracteres en un texto pero empezando por el final.