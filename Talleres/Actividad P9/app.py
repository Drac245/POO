from AnalizadorLogs import AnalizadorLogs


if __name__ == '__main__':
    nombre_archivo = "trafico_web.log"
    analizador = AnalizadorLogs(nombre_archivo)
    estadisticas = analizador.procesar_logs()

    if "error" in estadisticas:
        print(estadisticas["error"])
    else:
        print("Número total de solicitudes recibidas:", estadisticas["total_solicitudes"])
        print("Número de solicitudes por método HTTP:", estadisticas["solicitudes_por_metodo"])
        print("Número de solicitudes por código de respuesta:", estadisticas["solicitudes_por_codigo"])
        print("Tamaño total de respuesta:", estadisticas["tamano_total_respuesta"])
        print("Tamaño promedio de respuesta por solicitud:", estadisticas["tamano_promedio_respuesta"])
        print("Las 10 URL más solicitadas:")
        for url, num_solicitudes in estadisticas["url_mas_solicitadas"].items():
            print(f"{url}: {num_solicitudes} solicitudes")
