# Ejemplo de herencia en clases
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enMarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enMarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta esta vacia"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enMarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.hcaballito)

class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

miMoto=Moto("Honda", "GSX")
#miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Fiat", "Ducato")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos,Vehiculos):
    pass

# En este caso, al tener BicicletaElectrica herencia multiple, los objetos que se crean seria con el constructor de la primera clase puesta
miBici=BicicletaElectrica()
