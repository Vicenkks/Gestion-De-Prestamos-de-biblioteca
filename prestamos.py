from conexion import SessionLocal
from modelos import Libro

def prestarLibro():
    with SessionLocal() as session:
        try:
            id = int(input("Ingrese el ID del libro: "))
        except ValueError:
            print("ID invalido")
            return
        libro = session.get(Libro, id)
        if libro is None:
            print("Libro no encontrado")
            return
        if libro.disponibles == 0:
            print("Libro sin stock")
            return

        libro.disponibles -= 1
        session.commit()
        print("Prestamo exitoso")