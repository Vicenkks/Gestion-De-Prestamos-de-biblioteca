from conexion import engine
from modelos import Base

def crear_tablas():
    Base.metadata.create_all(engine)