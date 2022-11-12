# Ejemplo de creacion de clases, con su constructor, sus metodos y la creacion de instancias de clase usando los metodos y atributos que tienen
class coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos
        if self.__enMarcha:
            chequeo=self.__chequeo_interno()
        if self.__enMarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enMarcha and chequeo==False:
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas. Un ancho de", self.__anchoChasis,"y un largo de", self.__largoChasis)

    def __chequeo_interno(self):
        print("Se va a realizar un chequeo interno")
        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"
        if self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas":
            return True
        else:
            return False
        
miCoche=coche()
# print("El largo del coche es: ",miCoche.largoChasis)
# print("El coche tiene",miCoche.ruedas,"ruedas")
print(miCoche.arrancar(True))
miCoche.estado()
print("A continuacion creamos el segundo objeto")
miCoche2=coche()
# print("El largo del coche es: ",miCoche2.largoChasis)
# print("El coche tiene",miCoche2.ruedas,"ruedas")
print(miCoche2.arrancar(False))
# miCoche2.__ruedas=2
miCoche2.estado()