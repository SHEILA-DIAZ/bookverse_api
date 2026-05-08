# 📚 BookVerse API

API REST con **Django** y **Django REST Framework** para gestionar una biblioteca virtual con libros y autores.

---

## 🛠️ Tecnologías usadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje principal |
| Django | Framework web |
| Django REST Framework | API REST |
| SQLite | Base de datos |
| Postman | Cliente de pruebas |

---

## ⚙️ Ejecutar el servidor

```bash
git clone https://github.com/SHEILA-DIAZ/bookverse_api.git
cd bookverse_api
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Disponible en: `http://127.0.0.1:8000/`

---

## 📌 Endpoints

### 👤 Autores — `/api/autores/`

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/autores/` | Listar autores |
| POST | `/api/autores/` | Crear autor |
| PUT | `/api/autores/{id}/` | Actualizar autor |
| DELETE | `/api/autores/{id}/` | Eliminar autor |

**POST — Body:**
```json
{
  "nombre": "Gabriel García Márquez",
  "nacionalidad": "Colombiana"
}
```
**Respuesta `201 Created`:**
```json
{
  "id": 1,
  "nombre": "Gabriel García Márquez",
  "nacionalidad": "Colombiana"
}
```

---

### 📖 Libros — `/api/libros/`

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/libros/` | Listar libros |
| POST | `/api/libros/` | Crear libro |
| PUT | `/api/libros/{id}/` | Actualizar libro |
| PATCH | `/api/libros/{id}/` | Actualizar parcialmente |
| DELETE | `/api/libros/{id}/` | Eliminar libro |
| GET | `/api/libros/?search=` | Buscar por título o género |

**POST — Body:**
```json
{
  "titulo": "Cien años de soledad",
  "anio_publicacion": 1967,
  "genero": "Realismo mágico",
  "autor": 1
}
```

**Respuesta `201 Created`:**
```json
{
  "id": 1,
  "titulo": "Cien años de soledad",
  "anio_publicacion": 1967,
  "genero": "Realismo mágico",
  "autor": 1,
  "autor_nombre": "Gabriel García Márquez",
  "autor_nacionalidad": "Colombiana"
}
```

> ✨ **Punto extra:** la respuesta incluye `autor_nombre` y `autor_nacionalidad` de la entidad relacionada.

**Búsqueda:**
```bash
GET http://127.0.0.1:8000/api/libros/?search=Novela
GET http://127.0.0.1:8000/api/libros/?search=soledad
```

---

## 🖼️ Capturas

### 01 — Servidor Django
![Servidor Django](docs/capturas/01.png)

### 02 — Estructura del proyecto
![Estructura Proyecto](docs/capturas/02.png)

### 03 — models.py
![Models](docs/capturas/03.png)

### 04 — serializers.py
![Serializers](docs/capturas/04.png)

### 05 — views.py
![Views](docs/capturas/05.png)

### 06 — GET /api/autores/
![GET Autores](docs/capturas/06.png)

### 07 — POST /api/autores/
![POST Autor](docs/capturas/07.png)

### 08 — POST /api/libros/
![POST Libro](docs/capturas/08.png)

### 09 — Búsqueda ?search=Novela
![Search Libro](docs/capturas/09.png)

### 10 — Repositorio GitHub
![GitHub](docs/capturas/10.png)