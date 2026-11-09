
from conexion import SessionLocal
from modelos import Libro

def actualizarLibro():
    with SessionLocal() as session:
        try:
            id = int(input("Ingrese el ID del libro"))
        except ValueError:
            print("ID invalido")
            return
        libro = session.get(Libro, id)
        
        if libro is None:
            print("Libro no encontrado")
            return

        try:
            titulo = input("Nuevo título: ")
            autor = input("Nuevo autor: ")
            anio = int(input("Nuevo año: "))
            disponibles = int(input("Disponibilidad: "))

        except ValueError:
            print("El año y la disponibilidad deben ser números")
            return

        if anio <= 0 or disponibles < 0:
            print("Año o disponibilidad inválidos")
            return

        libro.titulo = titulo
        libro.autor = autor
        libro.anio = anio
        libro.disponibles = disponibles

        session.commit()
        print("Libro actualizado correctamente")
