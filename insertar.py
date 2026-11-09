from conexion import SessionLocal
from modelos import Libro

def registrar_Libro():
    with SessionLocal() as session:
        
        try:
            titulo = input("Título a registrar: ")
            autor = input("autor: ")
            anio = int(input("año: "))
            disponibles = int(input("Disponibilidad: "))

        except ValueError:
            print("El año y la disponibilidad deben ser números")
            return

        if anio <= 0 or disponibles < 0:
            print("Año o disponibilidad inválidos")
            return
        libro = Libro(titulo=titulo, autor=autor, anio=anio, disponibles=disponibles)

        session.add(libro)
        session.commit()
        print("Libro registrado")