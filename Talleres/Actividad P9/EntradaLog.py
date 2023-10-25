class EntradaLog:
    def __init__(self, ip, fecha_hora, metodo, url, codigo_respuesta, tamano_respuesta):
        self.ip = ip
        self.fecha_hora = fecha_hora
        self.metodo = metodo
        self.url = url
        self.codigo_respuesta = codigo_respuesta
        self.tamano_respuesta = int(tamano_respuesta)