import tkinter as tk
from tkinter import messagebox
from lapicero import Lapicero
from cliente import Cliente

clientes = []
lapiceros = []

lapicero1 = Lapicero(1, "BIC", "Azul")
lapicero2 = Lapicero(2, "Pilot", "Negro")
lapicero3 = Lapicero(3, "Faber-Castell", "Rojo")
lapicero4 = Lapicero(4, "BIC", "Negro")
lapicero5 = Lapicero(5, "BIC", "Rojo")
lapicero6 = Lapicero(6, "Faber-Castell", "Azul")
lapicero7 = Lapicero(7, "Faber-Castell", "Negro")
lapicero8 = Lapicero(8, "Paper Mate", "Azul")
lapicero9 = Lapicero(9, "Paper Mate", "Rojo")

lapiceros.extend([lapicero1, lapicero2, lapicero3, lapicero4, lapicero5, lapicero6, lapicero7, lapicero8, lapicero9])

def mostrar_menu():
    print("Menú:")
    print("1. Crear cliente")
    print("2. Alquilar lapicero")
    print("3. Devolver lapicero")
    print("4. Salir")

def mostrar_lapiceros_disponibles():
    print("Lapiceros disponibles:")
    for lapicero in lapiceros:
        if lapicero.disponible:
            print(f"ID: {lapicero.id_lapicero}, Marca: {lapicero.marca}, Color: {lapicero.color}")

class Interfaz:
    def __init__(self, root, clientes, lapiceros):
        self.root = root
        self.clientes = clientes
        self.lapiceros = lapiceros
        self.root.title("Alquiler de Lapiceros")

        self.boton_crear_cliente = tk.Button(self.root, text="Crear cliente", command=self.crear_cliente)
        self.boton_crear_cliente.pack()

        self.boton_alquilar_lapicero = tk.Button(self.root, text="Alquilar lapicero", command=self.alquilar_lapicero)
        self.boton_alquilar_lapicero.pack()

        self.boton_devolver_lapicero = tk.Button(self.root, text="Devolver lapicero", command=self.devolver_lapicero)
        self.boton_devolver_lapicero.pack()

    def crear_cliente(self):
        ventana_crear_cliente = tk.Toplevel(self.root)
        ventana_crear_cliente.title("Crear Cliente")

        etiqueta_nombre = tk.Label(ventana_crear_cliente, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_crear_cliente)
        entrada_nombre.pack()

        etiqueta_apellido = tk.Label(ventana_crear_cliente, text="Apellido:")
        etiqueta_apellido.pack()

        entrada_apellido = tk.Entry(ventana_crear_cliente)
        entrada_apellido.pack()

        boton_guardar = tk.Button(ventana_crear_cliente, text="Guardar", command=lambda: self.guardar_cliente(entrada_nombre.get(), entrada_apellido.get(), ventana_crear_cliente))
        boton_guardar.pack()

    def guardar_cliente(self, nombre, apellido, ventana):
        nuevo_cliente = Cliente(len(self.clientes) + 1, nombre, apellido)
        self.clientes.append(nuevo_cliente)
        ventana.destroy()
        messagebox.showinfo("Información", "Cliente creado con éxito")

    def alquilar_lapicero(self):
        ventana_alquilar_lapicero = tk.Toplevel(self.root)
        ventana_alquilar_lapicero.title("Alquilar Lapicero")

        etiqueta_cliente_id = tk.Label(ventana_alquilar_lapicero, text="ID del Cliente:")
        etiqueta_cliente_id.pack()

        entrada_cliente_id = tk.Entry(ventana_alquilar_lapicero)
        entrada_cliente_id.pack()

        etiqueta_lapicero_id = tk.Label(ventana_alquilar_lapicero, text="ID del Lapicero:")
        etiqueta_lapicero_id.pack()

        entrada_lapicero_id = tk.Entry(ventana_alquilar_lapicero)
        entrada_lapicero_id.pack()

        boton_alquilar = tk.Button(ventana_alquilar_lapicero, text="Alquilar", command=lambda: self.guardar_alquiler(entrada_cliente_id.get(), entrada_lapicero_id.get(), ventana_alquilar_lapicero))
        boton_alquilar.pack()

    def guardar_alquiler(self, cliente_id, lapicero_id, ventana):
        cliente = next((c for c in self.clientes if c.id_cliente == int(cliente_id)), None)
        lapicero = next((l for l in self.lapiceros if l.id_lapicero == int(lapicero_id) and l.disponible), None)

        if cliente and lapicero:
            if cliente.alquilar_lapicero(lapicero):
                ventana.destroy()
                messagebox.showinfo("Información", "Lapicero alquilado con éxito")
            else:
                messagebox.showerror("Error", "El lapicero seleccionado no está disponible.")
        else:
            messagebox.showerror("Error", "Cliente o lapicero no encontrado o lapicero no disponible.")

    def devolver_lapicero(self):
        ventana_devolver_lapicero = tk.Toplevel(self.root)
        ventana_devolver_lapicero.title("Devolver Lapicero")

        etiqueta_cliente_id = tk.Label(ventana_devolver_lapicero, text="ID del Cliente:")
        etiqueta_cliente_id.pack()

        entrada_cliente_id = tk.Entry(ventana_devolver_lapicero)
        entrada_cliente_id.pack()

        etiqueta_lapicero_id = tk.Label(ventana_devolver_lapicero, text="ID del Lapicero:")
        etiqueta_lapicero_id.pack()

        entrada_lapicero_id = tk.Entry(ventana_devolver_lapicero)
        entrada_lapicero_id.pack()

        boton_devolver = tk.Button(ventana_devolver_lapicero, text="Devolver", command=lambda: self.guardar_devolucion(entrada_cliente_id.get(), entrada_lapicero_id.get(), ventana_devolver_lapicero))
        boton_devolver.pack()

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root, clientes, lapiceros)
    root.mainloop()