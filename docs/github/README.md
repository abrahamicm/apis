## Introducción a la API de GitHub

La [API de GitHub](https://docs.github.com/en/rest) te permite interactuar con GitHub para realizar operaciones como acceder a repositorios, gestionar issues y controlar usuarios. Esta API es RESTful, permitiendo operaciones a través de peticiones HTTP estándar.

### Funcionalidades Principales

- **Repositorios:** Accede a detalles de repositorios, ramas, commits y colaboradores.
- **Issues:** Crea, lee, actualiza y cierra issues en repositorios.
- **Pull Requests:** Gestiona la creación, revisión y fusión de pull requests.
- **Usuarios:** Consulta información sobre usuarios y organizaciones.
- **Gists:** Crea y gestiona fragmentos de código o texto compartidos.

### Autenticación

Para usar la API, necesitas un token de acceso personal. [Genera tu token](https://github.com/settings/tokens) siguiendo estos pasos:

1. **Inicia sesión en GitHub:**
   - Accede a [GitHub](https://github.com/) e inicia sesión.

2. **Accede a Configuración:**
   - Haz clic en tu foto de perfil y selecciona **"Settings"**.

3. **Genera un Token:**
   - En el menú de la izquierda, selecciona **"Developer settings"** y luego **"Personal access tokens"**.
   - Haz clic en **"Generate new token"**.
   - Asigna un nombre al token y selecciona los permisos necesarios (por ejemplo, `repo` para acceso completo a repositorios).

4. **Copia el Token:**
   - Guarda el token en un lugar seguro. No podrás verlo nuevamente después de salir de la página.

### Ejemplos de Uso

#### Obtener Información de un Repositorio

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     https://api.github.com/repos/OWNER/REPO
```

#### Crear un Issue

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -d '{"title": "Bug en la aplicación", "body": "Descripción del problema"}' \
     https://api.github.com/repos/OWNER/REPO/issues
```

#### Listar Repositorios

- **De un Usuario:**

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     https://api.github.com/users/USERNAME/repos
```

- **De una Organización:**

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     https://api.github.com/orgs/ORG_NAME/repos
```

#### Crear un Repositorio

```bash
curl -H "Authorization: token YOUR_GITHUB_TOKEN" \
     -d '{"name": "nuevo-repositorio", "description": "Descripción del nuevo repositorio", "private": false}' \
     https://api.github.com/user/repos
```

### Documentación

Para más detalles sobre todos los endpoints y opciones disponibles, consulta la [documentación oficial de la API de GitHub](https://docs.github.com/en/rest).

### Seguridad del Token

Manten el token en secreto y no lo compartas. Si crees que tu token ha sido comprometido, revócalo inmediatamente desde la sección de **Personal access tokens** en GitHub.

---

¿Te parece bien así o hay algo más que te gustaría ajustar?