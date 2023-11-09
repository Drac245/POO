# Alquiler de Lapiceros

Este programa te permite alquilar lapiceros de manera simple desde una consola de comandos.

## Requisitos

Asegúrate de tener Python 3 instalado en tu sistema.

## Uso

1. Se mostrará un menú con las siguientes opciones:

- **Crear cliente:** Permite crear un nuevo cliente proporcionando su nombre y apellido.
- **Alquilar lapicero:** Permite alquilar un lapicero existente a un cliente registrado.
- **Devolver lapicero:** Permite a un cliente devolver un lapicero previamente alquilado.
- **Salir:** Cierra el programa.

2. Sigue las instrucciones en pantalla para seleccionar una opción y realizar las operaciones correspondientes.

¡Disfruta usando el programa de alquiler de lapiceros!








Clase Cliente
--------------
- id_cliente: int
- nombre: str
- apellido: str
- lapiceros_alquilados: list

+ alquilar_lapicero(lapicero: Lapicero): bool
+ devolver_lapicero(lapicero: Lapicero): bool


Clase Lapicero
--------------
- id_lapicero: int
- marca: str
- color: str
- disponible: bool


Clase Interfaz
--------------
- root: tk.Tk
- clientes: list
- lapiceros: list
- ventana_lapiceros_disponibles: tk.Toplevel
- ventana_clientes: tk.Toplevel

+ mostrar_lapiceros_disponibles(): None
+ mostrar_clientes(): None
+ crear_cliente(): None
+ guardar_cliente(nombre: str, apellido: str, ventana: tk.Toplevel): None
+ alquilar_lapicero(): None
+ guardar_alquiler(cliente_id: str, lapicero_id: str, ventana: tk.Toplevel): None
+ devolver_lapicero(): None
+ guardar_devolucion(cliente_id: str, lapicero_id: str, ventana: tk.Toplevel): None
