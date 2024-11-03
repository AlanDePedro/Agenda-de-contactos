

def mostrar_menu():
    print("\nAgenda de contactos")
    print("1. Agregar nuevo contacto")
    print("2. eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el telefono del contacto: ")
    email = input("Por favor agregue el mail del contacto: " )
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡se ha agregado el cacto {nombre} exitosamente")

def elimnar_contacto(agenda):
    nombre = input("ingre el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} fue eliminado correctamente")
    else:
        print(f"no se ha encontrado el contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]}")
        print(f"Email: {agenda[nombre]["email"]}")
    else:
        print(f"el contacto {nombre} no ha sido encontrado en la agenda")

def lista_contactos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda esta vacia")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opción = input("por favor elija una opción: ")
        print("\n")

        if opción == "1":
            agregar_contacto(agenda)
        elif opción == "2":
            elimnar_contacto(agenda)
        elif opción == "3":
            buscar_contacto(agenda)
        elif opción == "4":
            lista_contactos(agenda)
        elif opción == "5":
            print("Esta saliendo de la agenda, !Hasta Luego¡")
            break
        else:
            print("Selecionna una opcion valida por favor")

agenda_contactos()