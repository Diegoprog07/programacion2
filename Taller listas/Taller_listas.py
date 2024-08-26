a = []
l= list()   
l.append("jhon")
l.append("Juan")
l.append("Sebastian")

print("Menú:")
print("1. Crear persona")
print("2. Eliminar persona")
print("3. Listar personas")
print("4. Buscar persona")
print("5. Salir")

opcion = input("Ingrese una opción: ")

if opcion == "1":
    print(l)
    p=input("Ingresa el nombre de la persona que quiere agregar a la lista: ")
    l.append(p)
    print(l)
elif opcion == "2":
    print(l)
    R=input("Ingresa el nombre de la persona que quiere eliminar de la lista: ")
    l.remove(R)
    print(l)
elif opcion == "3":
    print(l)
elif opcion == "4":
    print(l)
    b=input("Ingresa el nombre de la persona que quiere buscar en la lista: ")
    if b in l:
        print("La persona está en la lista")
    else:
        print("La persona no está en la lista")
elif opcion == "5":
    print("Adiós")
else:
    print("Opción inválida. Por favor, ingrese una opción válida.")
