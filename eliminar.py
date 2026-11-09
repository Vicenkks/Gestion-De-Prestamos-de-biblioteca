from conexion import SessionLocal
from modelos import Libro

def eliminarLibro():
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
        session.delete(libro)
        session.commit()
        print("Libro eliminado correctamente")