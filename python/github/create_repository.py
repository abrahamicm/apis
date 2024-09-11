import os
import requests
from dotenv import load_dotenv

# Cargar el archivo .env que está dos carpetas arriba
dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

# Obtener el token de acceso del archivo .env
token = os.getenv('GITHUB_TOKEN')
if not token:
    raise ValueError("El token de GitHub no está configurado en el archivo .env")

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_repository(repo_name, description="", private=False):
    url = 'https://api.github.com/user/repos'
    data = {
        'name': repo_name,
        'description': description,
        'private': private
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print(f'Repositorio creado: {response.json()["html_url"]}')
    else:
        print(f'Error al crear el repositorio: {response.status_code}')
        print(response.json())

if __name__ == '__main__':
    # Ejemplo de uso
    repo_name = 'nuevo-repositorio'
    description = 'Descripción del nuevo repositorio'
    private = False
    
    create_repository(repo_name, description, private)
