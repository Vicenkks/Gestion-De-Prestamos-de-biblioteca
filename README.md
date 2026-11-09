# Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca desarrollado en **Python**, utilizando **SQLAlchemy ORM** y **SQLite** para administrar libros mediante una interfaz interactiva en la terminal.

Permite realizar operaciones **CRUD (Create, Read, Update, Delete)** y gestionar préstamos de libros, aplicando conceptos de programación orientada a objetos, bases de datos relacionales y desarrollo modular.

## Funcionalidades

- **Registrar libros:** Agregar nuevos libros indicando título, autor, año de publicación y cantidad disponible.
- **Consultar libros:** Visualizar todos los libros registrados en la base de datos.
- **Buscar libros por ID:** Obtener información de un libro específico.
- **Actualizar libros:** Modificar título, autor, año y disponibilidad.
- **Eliminar libros:** Eliminar registros de la base de datos.
- **Prestar libros:** Gestionar préstamos y actualizar la disponibilidad.
- **Validación de datos:** Verificar entradas numéricas y aplicar restricciones en la base de datos.

## 🛠️ Tecnologías utilizadas

- **Python 3:** Lenguaje principal.
- **SQLAlchemy ORM:** Interacción con la base de datos mediante objetos Python.
- **SQLite:** Base de datos relacional ligera.

## Estructura del proyecto

```text
biblioteca/
│
├── main.py
├── conexion.py
├── modelos.py
├── insertar.py
├── consultar.py
├── actualizar.py
├── eliminar.py
├── prestamos.py
├── biblioteca.db
└── README.md
```

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

### 2. Crear un entorno virtual

```bash
uv sync
```

## Ejecución
```bash
uv run python main.py
```

El sistema mostrará el siguiente menú:

```text
========== SISTEMA DE BIBLIOTECA ==========

1. Registrar libro
2. Consultar libros
3. Buscar libro por ID
4. Actualizar libro
5. Eliminar libro
6. Prestar libro
0. Salir

Seleccione una opción:
```

## Modelo de datos

El sistema utiliza una tabla llamada `Libro` con los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| id | Integer | Identificador único |
| titulo | String(150) | Título del libro |
| autor | String(100) | Autor del libro |
| anio | Integer | Año de publicación |
| disponibles | Integer | Ejemplares disponibles |

### Restricciones

- El año debe ser mayor que cero.
- La disponibilidad no puede ser negativa.
- El título y el autor son campos obligatorios.

## Ejemplo de uso

### Registrar un libro

```text
Seleccione una opción: 1

Título a registrar: Harry Potter
Autor: Joanne Rowling
Año: 2005
Disponibilidad: 5

Libro registrado
```

### Consultar libros

```text
Seleccione una opción: 2

(Libro: id=1, titulo=Harry Potter, autor=Joanne Rowling)
```

### Actualizar un libro

```text
Seleccione una opción: 4

ID del libro: 1
Nuevo título: Harry Potter
Nuevo autor: Joanne Rowling
Nuevo año: 2005
Disponibilidad: 10

Libro actualizado
```

## Posibles mejoras

- [ ] Implementar búsqueda de libros por título o autor.
- [ ] Evitar el registro de libros duplicados.
- [ ] Incorporar un historial de préstamos.
- [ ] Registrar usuarios de la biblioteca.
- [ ] Implementar devolución de libros.
- [ ] Agregar pruebas automatizadas.
- [ ] Desarrollar una API REST con FastAPI.