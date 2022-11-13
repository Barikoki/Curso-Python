# Importando de esta forma tendriamos que usar las funciones con el nombre del modulo delante
import Funciones_Matematicas

Funciones_Matematicas.sumar(7,2)
Funciones_Matematicas.restar(9,5)

# Con esta otra forma importamos todo el contenido del modulo y no tenemos la necesidad de poner el nombre del modulo delante
from Funciones_Matematicas import *
sumar(7,5)
restar(6,3)
multiplicar(5,6)