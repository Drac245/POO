from lapicero import Lapicero
from cliente import Cliente

# Crear una lista para almacenar clientes
clientes = []

# Crear algunos lapiceros
lapicero1 = Lapicero(1, "BIC", "Azul")
lapicero2 = Lapicero(2, "Pilot", "Negro")
lapicero3 = Lapicero(3, "Faber-Castell", "Rojo")

# Función para mostrar el menú y procesar las opciones del usuario
def mostrar_menu():
    print("Menú:")
    print("1. Crear cliente")
    print("2. Alquilar lapicero")
    print("3. Devolver lapicero")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Crear cliente
            nombre = input("Ingrese el nombre del nuevo cliente: ")
            apellido = input("Ingrese el apellido del nuevo cliente: ")
            nuevo_cliente = Cliente(len(clientes) + 1, nombre, apellido)
            clientes.append(nuevo_cliente)
            print(f"Cliente {nombre} {apellido} creado con ID {nuevo_cliente.id_cliente}")

        elif opcion == "2":
            # Alquilar lapicero
            if not clientes:
                print("No hay clientes registrados. Debe crear un cliente primero.")
                continue

            # Mostrar lapiceros disponibles
            print("Lapiceros disponibles:")
            for lapicero in [lapicero1, lapicero2, lapicero3]:
                if lapicero.disponible:
                    print(f"ID: {lapicero.id_lapicero}, Marca: {lapicero.marca}, Color: {lapicero.color}")

            cliente_id = int(input("Ingrese el ID del cliente que desea alquilar: "))
            lapicero_id = int(input("Ingrese el ID del lapicero que desea alquilar: "))

            # Buscar el cliente y el lapicero en la lista
            cliente = None
            for c in clientes:
                if c.id_cliente == cliente_id:
                    cliente = c
                    break

            lapicero = None
            for l in [lapicero1, lapicero2, lapicero3]:
                if l.id_lapicero == lapicero_id and l.disponible:
                    lapicero = l
                    break

            if cliente and lapicero:
                if cliente.alquilar_lapicero(lapicero):
                    print(f"Lapicero {lapicero.marca} alquilado por {cliente.nombre} {cliente.apellido}")
                else:
                    print("El lapicero seleccionado no está disponible.")
            else:
                print("Cliente o lapicero no encontrado o lapicero no disponible.")

        elif opcion == "3":
            # Devolver lapicero (código existente)
            cliente_id = int(input("Ingrese el ID del cliente: "))
            lapicero_id = int(input("Ingrese el ID del lapicero que desea devolver: "))

            # Buscar el cliente y el lapicero en la lista
            cliente = None
            for c in clientes:
                if c.id_cliente == cliente_id:
                    cliente = c
                    break
            
            lapicero = None
            for l in [lapicero1, lapicero2, lapicero3]:
                if l.id_lapicero == lapicero_id and not l.disponible:
                    lapicero = l
                    break
            
            if cliente and lapicero:
                if cliente.devolver_lapicero(lapicero):
                    print(f"Lapicero {lapicero.marca} devuelto por {cliente.nombre} {cliente.apellido}")
                else:
                    print("El lapicero seleccionado no fue alquilado por este cliente o no está en su lista de alquileres.")
            else:
                print("Cliente o lapicero no encontrado o lapicero no fue alquilado por este cliente.")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
