from conexion import engine
from modelos import Base, Libro
from crear_tablas import crear_tablas
from insertar import registrar_Libro
from consultar import consultarLibroId, consultarLibros
from actualizar import actualizarLibro
from eliminar import eliminarLibro
from prestamos import prestarLibro

opciones = {
    "1" : registrar_Libro,
    "2" : consultarLibros,
    "3" : consultarLibroId,
    "4" : actualizarLibro,
    "5" : eliminarLibro,
    "6" : prestarLibro,
}


if __name__ == "__main__":
    crear_tablas()
    while True:
        print(
            """
            ========== SISTEMA DE BIBLIOTECA ==========
            1. Registrar libro
            2. Consultar libros
            3. Buscar libro por ID
            4. Actualizar libro
            5. Eliminar libro
            6. Prestar libro
            0. Salir
            """
        )
        opcion = input("Seleccione una opción: ")
        if int(opcion) == 0:
            break
        elif opcion not in opciones:
            print("Opcion invalida")
        else: opciones[opcion]()
