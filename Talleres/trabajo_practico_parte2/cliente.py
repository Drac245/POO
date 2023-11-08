class Cliente:
    def __init__(self, id_cliente, nombre, apellido):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.lapiceros_alquilados = []

    def alquilar_lapicero(self, lapicero):
        if lapicero.disponible:
            lapicero.disponible = False
            self.lapiceros_alquilados.append(lapicero)
            return True
        return False

    def devolver_lapicero(self, lapicero):
        if lapicero in self.lapiceros_alquilados:
            lapicero.disponible = True
            self.lapiceros_alquilados.remove(lapicero)
            return True
        return False
