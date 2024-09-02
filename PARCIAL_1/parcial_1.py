class PERSONA:
    def __init__(self, nombre, apellido, direccion, telefono, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_apellido(self):
        return self.apellido
    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono
    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_edad(self):
        return self.edad
    def set_edad(self, edad):
        self.edad = edad

    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email


class EMPLEADO(PERSONA):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, NombreCargo, Salario, JefeInmediato, años_experiencia):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.NombreCargo = NombreCargo
        self.Salario = Salario
        self.JefeInmediato = JefeInmediato
        self.años_experiencia = años_experiencia

    def get_NombreCargo(self):
        return self.NombreCargo
    def set_NombreCargo(self, NombreCargo):
        self.NombreCargo = NombreCargo

    def get_Salario(self):
        return self.Salario
    def set_Salario(self, Salario):
        self.Salario = Salario
        
    def get_JefeInmediato(self):
        return self.JefeInmediato
    def set_JefeInmediato(self, JefeInmediato):
        self.JefeInmediato = JefeInmediato

    def get_años_experiencia(self):
        return self.años_experiencia
    def set_años_experiencia(self, años_experiencia):
        self.años_experiencia = años_experiencia

def cargo(EMPLEADO):
    if EMPLEADO.get_Salario() >= 5000000 and EMPLEADO.get_años_experiencia() >= 5 and 25 <= EMPLEADO.get_edad() <= 45:
        EMPLEADO.set_NombreCargo("Senior")
    elif 900000 <= EMPLEADO.get_Salario() <= 1200000 and 1 <= EMPLEADO.get_años_experiencia() <= 2 and 18 <= EMPLEADO.get_edad() <= 22:
        EMPLEADO.set_NombreCargo("Junior")
    else:
        EMPLEADO.set_NombreCargo("No tiene cargo")
        
nombre = input("Ingrese el nombre:")
apellido = input("Ingrese el apellido:")
direccion = input("Ingrese la dirección:")
telefono = input("Ingrese el telefono:")
edad = int(input("Ingrese la edad:"))
email = input("Ingrese el email:")
salario = float(input("Ingrese el salario:"))
jefe_inmediato = input("Ingrese el jefe inmediato:")
años_experiencia = int(input("Ingrese los años de experiencia:"))

EMPLEADO = EMPLEADO(nombre, apellido, direccion, telefono, edad, email, "", salario, jefe_inmediato, años_experiencia)
cargo(EMPLEADO)

print("Detalle del Empleado:")
print("Nombre:", EMPLEADO.get_nombre())
print("Apellido:", EMPLEADO.get_apellido())
print("Dirección:", EMPLEADO.get_direccion())
print("Telefono:", EMPLEADO.get_telefono())
print("Edad:", EMPLEADO.get_edad())
print("Email:", EMPLEADO.get_email())
print("Cargo:", EMPLEADO.get_NombreCargo())