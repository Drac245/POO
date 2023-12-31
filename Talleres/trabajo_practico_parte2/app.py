import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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

class Interfaz:
    def __init__(self, root, clientes, lapiceros):
        self.root = root
        self.clientes = clientes
        self.lapiceros = lapiceros
        self.root.title("Alquiler de Lapiceros")

        style = ttk.Style()
        style.configure("BW.TButton", foreground="black", background="white", font=("Arial", 20), padding=10)

        self.boton_crear_cliente = tk.Button(self.root, text="Crear cliente", command=self.crear_cliente)
        self.boton_crear_cliente.pack()
        self.boton_crear_cliente.pack(pady=10)

        self.boton_alquilar_lapicero = tk.Button(self.root, text="Alquilar lapicero", command=self.alquilar_lapicero)
        self.boton_alquilar_lapicero.pack()
        self.boton_alquilar_lapicero.pack(pady=10)

        self.boton_devolver_lapicero = tk.Button(self.root, text="Devolver lapicero", command=self.devolver_lapicero)
        self.boton_devolver_lapicero.pack()
        self.boton_devolver_lapicero.pack(pady=10)

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
        if not nombre or not apellido:
            messagebox.showerror("Error", "El nombre y el apellido no pueden estar vacíos.")
            return

        nuevo_cliente = Cliente(len(self.clientes) + 1, nombre, apellido)
        self.clientes.append(nuevo_cliente)
        ventana.destroy()
        messagebox.showinfo("Información", f"Cliente creado con éxito. ID del cliente: {nuevo_cliente.id_cliente}")


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

        if not cliente_id.isdigit() or not lapicero_id.isdigit():
            messagebox.showerror("Error", "Las IDs del cliente y del lapicero deben ser números enteros.")
            return
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

    def mostrar_lapiceros_disponibles(self):

        for widget in self.ventana_lapiceros_disponibles.winfo_children():
            widget.destroy()

        for lapicero in self.lapiceros:
            if lapicero.disponible:
                etiqueta_lapicero = tk.Label(self.ventana_lapiceros_disponibles, text=f"ID: {lapicero.id_lapicero}, Marca: {lapicero.marca}, Color: {lapicero.color}")
                etiqueta_lapicero.pack()

        self.root.after(2000, self.mostrar_lapiceros_disponibles)

    def guardar_devolucion(self, cliente_id, lapicero_id, ventana):
        cliente = next((c for c in self.clientes if c.id_cliente == int(cliente_id)), None)
        lapicero = next((l for l in self.lapiceros if l.id_lapicero == int(lapicero_id) and not l.disponible), None)

        if cliente and lapicero:
            if cliente.devolver_lapicero(lapicero):
                ventana.destroy()
                messagebox.showinfo("Información", "Lapicero devuelto con éxito")
            else:
                messagebox.showerror("Error", "El cliente no ha alquilado el lapicero seleccionado.")
        else:
            messagebox.showerror("Error", "Cliente o lapicero no encontrado o lapicero ya está disponible.")

    def mostrar_clientes(self):
        for widget in self.ventana_clientes.winfo_children():
            widget.destroy()

        for cliente in self.clientes:
            etiqueta_cliente = tk.Label(self.ventana_clientes, text=f"ID: {cliente.id_cliente}, Nombre: {cliente.nombre}, Apellido: {cliente.apellido}")
            etiqueta_cliente.pack()
            for lapicero in cliente.lapiceros_alquilados:
                etiqueta_lapicero = tk.Label(self.ventana_clientes, text=f"    Lapicero alquilado - ID: {lapicero.id_lapicero}, Marca: {lapicero.marca}, Color: {lapicero.color}")
                etiqueta_lapicero.pack()

        self.root.after(2000, self.mostrar_clientes)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200+0+0") 

    interfaz = Interfaz(root, clientes, lapiceros)

    interfaz.ventana_lapiceros_disponibles = tk.Toplevel(root)
    interfaz.ventana_lapiceros_disponibles.geometry("300x200+500+0") 
    interfaz.ventana_lapiceros_disponibles.title("Lapiceros Disponibles")
    interfaz.mostrar_lapiceros_disponibles() 

    interfaz.ventana_clientes = tk.Toplevel(root)
    interfaz.ventana_clientes.geometry("300x400+1000+0")
    interfaz.ventana_clientes.title("Clientes y Lapiceros Alquilados")
    interfaz.mostrar_clientes() 

    root.mainloop()
