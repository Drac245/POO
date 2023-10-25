from typing import Dict, Any
from EntradaLog import EntradaLog

class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.entradas_logs = []

    def procesar_logs(self) -> Dict[str, Any]:
        try:
            with open(self.nombre_archivo, 'r') as file:
                registros = file.read().split('\n\n')  
                for registro in registros:
                    lines = registro.split('\n')

                    ip = lines[0].split(': ')[1]
                    fecha_hora = lines[1].split(': ')[1]
                    metodo = lines[2].split(': ')[1]
                    url = lines[3].split(': ')[1]
                    codigo_respuesta = int(lines[4].split(': ')[1])
                    tamano_respuesta = int(lines[5].split(': ')[1])

                    entrada_log = EntradaLog(ip, fecha_hora, metodo, url, codigo_respuesta, tamano_respuesta)
                    self.entradas_logs.append(entrada_log)

                total_solicitudes = len(self.entradas_logs)
                solicitudes_por_metodo = {}
                solicitudes_por_codigo = {}
                tamano_total_respuesta = 0
                url_solicitudes = {}
                # for para contar
                for entrada in self.entradas_logs:
                    if entrada.metodo in solicitudes_por_metodo:
                        solicitudes_por_metodo[entrada.metodo] += 1
                    else:
                        solicitudes_por_metodo[entrada.metodo] = 1

                    if entrada.codigo_respuesta in solicitudes_por_codigo:
                        solicitudes_por_codigo[entrada.codigo_respuesta] += 1
                    else:
                        solicitudes_por_codigo[entrada.codigo_respuesta] = 1

                    tamano_total_respuesta += entrada.tamano_respuesta

                    if entrada.url in url_solicitudes:
                        url_solicitudes[entrada.url] += 1
                    else:
                        url_solicitudes[entrada.url] = 1

                tamano_promedio_respuesta = tamano_total_respuesta / total_solicitudes

                url_mas_solicitadas = dict(sorted(url_solicitudes.items(), key=lambda item: item[1], reverse=True)[:10])

                estadisticas = {
                    "total_solicitudes": total_solicitudes,
                    "solicitudes_por_metodo": solicitudes_por_metodo,
                    "solicitudes_por_codigo": solicitudes_por_codigo,
                    "tamano_total_respuesta": tamano_total_respuesta,
                    "tamano_promedio_respuesta": tamano_promedio_respuesta,
                    "url_mas_solicitadas": url_mas_solicitadas
                }

                return estadisticas

        except FileNotFoundError:
            return {"error": "El archivo de logs no se encontró."}
