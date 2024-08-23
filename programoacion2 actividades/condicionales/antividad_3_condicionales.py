nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo(1 masculini/2 femenino): ")

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
if sexo == "1":
        print("Usted es un Hombre.")
else:
        print("Usted es una Mujer.")