class Usuario:
    def __init__(self, nombrecompleto, nickname, clave, tipo, fecha_creacion):
        self.datos = {
            "nombrecompleto": nombrecompleto,
            "nickname": nickname,
            "clave": clave,
            "tipo": tipo,
            "fecha_creacion": fecha_creacion
        }
    #como no especifico con que buscar el usuario, lo hice por nombre completo
    def buscar_usuario(self, nombrecompleto):
        if self.datos["nombrecompleto"] == nombrecompleto:
            return self.datos
        return None
    #como no especifico con que eliminar el usuario, lo hice por nombre completo
    def eliminar_usuario(self, nombrecompleto):
        if self.datos["nombrecompleto"] == nombrecompleto:
            return True
        else:
            return False


def agregar_usuario():
    nombrecompleto = input("Ingrese el nombre completo del usuario: ")
    nickname = input("Ingrese el nickname del usuario: ")
    clave = input("Ingrese la clave del usuario: ")    
    #como no especifico que poner en tipo puse administrador y usuario
    tipo = input("Ingrese el tipo de usuario (administrador o usuario): ")
    fecha_creacion = input("Ingrese la fecha de creación del usuario: ")

    usuario = Usuario(nombrecompleto, nickname, clave, tipo, fecha_creacion)
    return usuario


def menu():
    usuarios = []

    while True:
        print("----- MENÚ -----")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            usuario = agregar_usuario()
            usuarios.append(usuario)
            print("Usuario agregado exitosamente.")
        elif opcion == "2":
            nombrecompleto = input("Ingrese el nombre completo del usuario a buscar: ")
            for usuario in usuarios:
                if usuario.buscar_usuario(nombrecompleto):
                    print("Usuario encontrado:")
                    print(usuario.buscar_usuario(nombrecompleto))
                    break
            else:
                print("Usuario no encontrado.")
        elif opcion == "3":
            nombrecompleto = input("Ingrese el nombre completo del usuario a eliminar: ")
            for usuario in usuarios:
                if usuario.eliminar_usuario(nombrecompleto):
                    usuarios.remove(usuario)  
                    print("Usuario eliminado exitosamente.")
                    break
            else:
                print("Usuario no encontrado.")
        elif opcion == "4":
            break
        else:
            print("Opcion invalida. Por favor, ingrese una opcion valida.")


menu()