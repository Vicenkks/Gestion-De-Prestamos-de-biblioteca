from conexion import SessionLocal
from modelos import Libro
from sqlalchemy import select

def consultarLibroId():
    with SessionLocal() as session:
        try:
            id = int(input("Ingrese el ID del libro: "))
        except ValueError:
            print("ID invalido")
            return
        
        libro = session.get(Libro, id)
        if libro is not None:
            print(libro)

        else:
            print("Libro no encontrado")
        


def consultarLibros():
    with SessionLocal() as session:
        stmt = select(Libro)
        libros = session.scalars(stmt)
        for libro in libros:
            print(libro)