from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Integer, CheckConstraint
from conexion import engine

class Base(DeclarativeBase):
    pass

class Libro(Base):
    __tablename__ = "Libro"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    autor: Mapped[str] = mapped_column(String(100), nullable=False)
    anio: Mapped[int] = mapped_column(Integer, nullable=False)
    disponibles: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("anio > 0", name= "anio mayor que cero"),
        CheckConstraint("disponibles >= 0", name= "mayor o igual que cero"),
    )
    def __repr__(self) -> str:
        return f"""
        ---- Libro ----
        ID: {self.id}
        Titulo: {self.titulo}
        Autor: {self.autor}
        Año: {self.anio}
        Disponibilidad: {self.disponibles}"""
    


