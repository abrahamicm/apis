# Scripts en Python para GitHub API

Este directorio contiene scripts en Python para interactuar con la API de GitHub. Antes de ejecutar los scripts, asegúrate de instalar las dependencias necesarias.

## Requisitos

Los scripts requieren las siguientes bibliotecas de Python:

- `requests`: Para hacer solicitudes HTTP a la API de GitHub.
- `python-dotenv`: Para cargar variables de entorno desde un archivo `.env`.

## Instalación

1. **Crea un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Unix
   venv\Scripts\activate     # Para Windows
   ```

2. **Instala las dependencias:**

   ```bash
   pip install requests python-dotenv
   ```

## Uso

Asegúrate de tener un archivo `.env` en el directorio raíz del proyecto con el siguiente formato:

```env
GITHUB_TOKEN=your_github_token_here
```

### Ejecutar Scripts

Para ejecutar un script, usa el siguiente comando:

```bash
python nombre_del_script.py
```

Por ejemplo, para crear un nuevo repositorio:

```bash
python create_repository.py
```

## Ejemplos de Scripts

- **`create_repository.py`**: Crea un nuevo repositorio en tu cuenta de GitHub.
- **`list_repositories.py`**: Lista los repositorios de un usuario o una organización.
- **`get_repository_info.py`**: Obtiene información sobre un repositorio específico.

## Notas

- Asegúrate de que tu token de GitHub tenga los permisos necesarios para las operaciones que deseas realizar.
- Para más detalles sobre los scripts, revisa el código fuente y los comentarios dentro de los mismos.
