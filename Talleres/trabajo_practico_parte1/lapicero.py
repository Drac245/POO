class Lapicero:
    def __init__(self, id_lapicero, marca, color):
        self.id_lapicero = id_lapicero
        self.marca = marca
        self.color = color
        self.disponible = True  # Inicialmente, el lapicero está disponible

    def marcar_como_alquilado(self):
        self.disponible = False

    def marcar_como_disponible(self):
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Lapicero ID: {self.id_lapicero}, Marca: {self.marca}, Color: {self.color}, Estado: {estado}"
