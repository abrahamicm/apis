
# Permisos para los Repositorios

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `repo`                  | Control total de repositorios privados y públicos. Incluye la capacidad de crear, leer, actualizar y eliminar repositorios. |
| `public_repo`           | Acceso a repositorios públicos solamente. No suficiente para gestionar repositorios privados. |
| `repo:status`           | Acceso al estado de los commits.                                                 |
| `repo_deployment`       | Acceso al estado de los despliegues en los repositorios.                        |
| `repo:invite`           | Acceso a las invitaciones para colaborar en repositorios.                       |
| `delete_repo`           | Permite eliminar repositorios.                                                  |

# Permisos para Hooks de Repositorios

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `admin:repo_hook`       | Control total sobre los hooks de repositorio. Permite la gestión completa de los hooks configurados. |
| `write:repo_hook`       | Permite escribir o modificar los hooks del repositorio.                        |
| `read:repo_hook`        | Permite leer los hooks del repositorio, pero no modificarlos.                    |

# Permisos para Gists

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `gist`                  | Crear gists (fragmentos de código o texto).                                    |

# Permisos para Gestión de la Cuenta y Proyectos

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `admin:org`             | Control total sobre organizaciones, equipos y proyectos de la organización.    |
| `write:org`             | Leer y escribir membresías de organizaciones y equipos, y proyectos de la organización. |
| `read:org`              | Leer membresías de organizaciones y equipos, y proyectos de la organización.   |
| `project`               | Control total sobre los proyectos.                                              |
| `read:project`          | Leer acceso a los proyectos.                                                     |

# Permisos para Claves y Seguridad

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `admin:public_key`      | Control total sobre las claves públicas de los usuarios.                       |
| `write:public_key`      | Escribir claves públicas de usuarios.                                          |
| `read:public_key`       | Leer claves públicas de usuarios.                                               |
| `admin:gpg_key`         | Control total sobre las claves GPG públicas de los usuarios.                    |
| `write:gpg_key`         | Escribir claves GPG públicas de los usuarios.                                  |
| `read:gpg_key`          | Leer claves GPG públicas de los usuarios.                                       |
| `admin:ssh_signing_key` | Control total sobre las claves SSH de firma pública de los usuarios.            |
| `write:ssh_signing_key` | Escribir claves SSH de firma pública de los usuarios.                           |
| `read:ssh_signing_key`  | Leer claves SSH de firma pública de los usuarios.                               |

# Permisos para Paquetes y GitHub Actions

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `write:packages`        | Subir paquetes al registro de paquetes de GitHub.                              |
| `read:packages`         | Descargar paquetes del registro de paquetes de GitHub.                          |
| `delete:packages`       | Eliminar paquetes del registro de paquetes de GitHub.                           |
| `workflow`              | Actualizar flujos de trabajo de GitHub Actions.                                |

# Permisos para Notificaciones y Otros

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `notifications`         | Acceso a las notificaciones.                                                   |
| `user`                  | Actualizar todos los datos del usuario.                                        |
| `read:user`             | Leer todos los datos del perfil del usuario.                                   |
| `user:email`            | Acceso solo de lectura a las direcciones de correo electrónico del usuario.     |
| `user:follow`           | Seguir y dejar de seguir usuarios.                                              |
| `write:discussion`      | Leer y escribir discusiones de equipo.                                         |
| `read:discussion`       | Leer discusiones de equipo.                                                     |

# Permisos para Empresas y Billing

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `admin:enterprise`      | Control total sobre las empresas.                                              |
| `manage_runners:enterprise` | Gestionar corredores y grupos de corredores de la empresa.                       |
| `manage_billing:enterprise` | Leer y escribir datos de facturación de la empresa.                             |
| `read:enterprise`       | Leer datos del perfil de la empresa.                                            |

# Permisos para Runners y Copilot

| Alcance                 | Descripción en Español                                                      |
|-------------------------|------------------------------------------------------------------------------|
| `manage_runners:org`    | Gestionar corredores y grupos de corredores de la organización.                 |
| `codespace`             | Control total sobre los codespaces.                                             |
| `codespace:secrets`     | Crear, leer, actualizar y eliminar secretos de codespace.                       |
| `copilot`               | Control total sobre las configuraciones de GitHub Copilot y asignaciones de asientos. |
| `manage_billing:copilot` | Ver y editar asignaciones de asientos de Copilot Business.                       |
| `audit_log`             | Control total sobre el registro de auditoría.                                   |
| `read:audit_log`        | Leer acceso al registro de auditoría.                                           |
