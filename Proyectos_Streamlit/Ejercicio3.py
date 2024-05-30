"""
Cree un diccionario que contenga el Nombre de una ciudad, el país al que
pertenece y la cantidad de habitantes que tiene. Hacer un menú iterativo que
permita al usuario realizar las siguientes operaciones:

Agregar Ciudades
Eliminar Ciudades
Indicar la cantidad de habitantes en un país en particular
El porcentaje de habitantes en una ciudad de acuerdo al total registrado

"""
Ciudades = {
    "Mendoza": {"Pais": "Argentina", "Habitantes": 799100},
    "Sao Pablo": {"Pais": "Brasil", "Habitantes": 10292110},
    "Madrid": {"Pais": "España", "Habitantes": 21019230},
    "Barcelona": {"Pais": "España", "Habitantes": 4566190},
    "Paris": {"Pais": "Francia", "Habitantes": 29990},
}


def mostrar_menu():
    print("1. Agregar ciudad")
    print("2. Eliminar ciudad")
    print("3. Cantidad de habitantes en un país")
    print("4. Porcentaje de habitantes en una ciudad")
    print("5. Salir")


def agregar_ciudad():
    nombre = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el país al que pertenece: ")
    habitantes = int(input("Ingrese la cantidad de habitantes: "))
    Ciudades[nombre] = {"Pais": pais, "Habitantes": habitantes}


def eliminar_ciudad():
    nombre = input("Ingrese el nombre de la ciudad a eliminar: ")
    if nombre in Ciudades:
        del Ciudades[nombre]
        print(f"{nombre} ha sido eliminada.")
    else:
        print(f"{nombre} no se encuentra en la lista.")


def cantidad_habitantes_pais():
    pais = input("Ingrese el país para consultar la cantidad de habitantes: ")
    total_habitantes = sum(
        ciudad["Habitantes"] for ciudad in Ciudades.values() if ciudad["Pais"] == pais)
    print(f"La cantidad total de habitantes en {pais} es: {total_habitantes}")


def porcentaje_habitantes_ciudad():
    nombre = input(
        "Ingrese el nombre de la ciudad para calcular el porcentaje: ")
    if nombre in Ciudades:
        habitantes_ciudad = Ciudades[nombre]["Habitantes"]
        total_habitantes = sum(ciudad["Habitantes"]
                               for ciudad in Ciudades.values())
        porcentaje = (habitantes_ciudad / total_habitantes) * 100
        print(f"El porcentaje de habitantes en {nombre} es: {porcentaje:.2f}%")
    else:
        print(f"{nombre} no se encuentra en la lista.")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_ciudad()
    elif opcion == "2":
        eliminar_ciudad()
    elif opcion == "3":
        cantidad_habitantes_pais()
    elif opcion == "4":
        porcentaje_habitantes_ciudad()
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
