class Persona():
    def __init__(self, Nombre, Edad, Lugar_residencia):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("Nombre:",self.Nombre,"Edad:",self.Edad,"Residencia:",self.Lugar_residencia)

class Empleado(Persona):
    def __init__(self, Salario, Antiguedad, Nombre_Empleado, Edad_Empleado, Residencia_Empleado):
        super().__init__(Nombre_Empleado, Edad_Empleado, Residencia_Empleado)
        self.Salario=Salario
        self.Antiguedad=Antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario:",self.Salario,"Antiguedad:",self.Antiguedad)

Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()
print(isinstance(Manuel, Empleado))

Manuel2=Persona("Manuel2", 26, "Argentina")
print(isinstance(Manuel2, Empleado))