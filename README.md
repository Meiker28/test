# FastAPI Date Counter

Este proyecto es una API construida con FastAPI que proporciona la fecha actual en diferentes formatos y cuenta el número de veces que ha sido llamada.

## 🚀 Características
- **POST /get_date**: Retorna la fecha actual en formato detallado o simplificado según un parámetro booleano.
- **GET /counter**: Devuelve la cantidad de veces que se ha llamado cualquiera de los dos endpoints.
- Implementado con **FastAPI** y ejecutable en un contenedor **Docker**.

## 📦 Instalación y Ejecución
### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

### 2️⃣ Crear un entorno virtual (opcional)
```sh
python -m venv env
source env/bin/activate  # En macOS/Linux
env\Scripts\activate     # En Windows
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Ejecutar la aplicación localmente
```sh
uvicorn main:app --reload
```
La API estará disponible en: [http://localhost:8000](http://localhost:8000)

## 🐳 Ejecución con Docker
### 1️⃣ Construir la imagen
```sh
docker build -t fastapi-app .
```

### 2️⃣ Ejecutar el contenedor
```sh
docker run -p 8000:8000 fastapi-app
```

## 📖 Endpoints
### `POST /get_date`
- **Parámetro:** `detailed` (booleano)
- **Ejemplo de request:**
  ```sh
  curl -X 'POST' 'http://localhost:8000/get_date' \
       -H 'Content-Type: application/json' \
       -d '{"detailed": true}'
  ```
- **Ejemplo de respuesta:**
  ```json
  { "date": "2025-02-19 14:30:00" }
  ```

### `GET /counter`
- **Ejemplo de request:**
  ```sh
  curl -X 'GET' 'http://localhost:8000/counter'
  ```
- **Ejemplo de respuesta:**
  ```json
  { "count": 5 }
  ```

## 📜 Documentación automática
FastAPI genera documentación interactiva:
- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

## ✨ Contribuciones
Si deseas mejorar este proyecto, ¡las contribuciones son bienvenidas! Crea un *fork*, haz tus cambios y envía un *pull request*.

## 📄 Licencia
Este proyecto está bajo la licencia MIT. ¡Disfrútalo! 🚀


