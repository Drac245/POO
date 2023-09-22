class Cliente:
    def __init__(self, id_cliente, nombre, apellido):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.lapiceros_alquilados = []

    def alquilar_lapicero(self, lapicero):
        if lapicero.disponible:
            lapicero.marcar_como_alquilado()
            self.lapiceros_alquilados.append(lapicero)
            return True
        else:
            return False

    def devolver_lapicero(self, lapicero):
        if lapicero in self.lapiceros_alquilados:
            lapicero.marcar_como_disponible()
            self.lapiceros_alquilados.remove(lapicero)
            return True
        else:
            return False

    def __str__(self):
        return f"Cliente ID: {self.id_cliente}, Nombre: {self.nombre}, Apellido: {self.apellido}"
