# Sistema CRUD con Autenticación en Flask

Este es un proyecto de práctica diseñado para demostrar la implementación básica de operaciones CRUD (Create, Read, Update, Delete) con un sistema de autenticación de usuarios utilizando Flask y MySQL.

## ⚠️ Aviso Importante

Este es un proyecto de práctica y aprendizaje, **NO está diseñado para uso en producción**. Carece de importantes medidas de seguridad como:
- Protección contra inyección SQL
- Protección contra ataques CSRF
- Validaciones exhaustivas de entrada
- Encriptación avanzada

## 🎯 Propósito

El objetivo principal de este proyecto es servir como base de aprendizaje para entender:
- Implementación de operaciones CRUD básicas
- Sistema de autenticación de usuarios
- Manejo de sesiones
- Interacción con bases de datos MySQL
- Estructuración de una aplicación Flask

## 🛠️ Tecnologías Utilizadas

- Python
- Flask
- MySQL
- HTML
- Bootstrap (para estilos básicos)

## 📁 Estructura del Proyecto

```
CRUD+Auth/
│
├── app.py              # Archivo principal con las rutas y lógica
├── schema.db         # Base de datos MySQL
├── templates/          # Plantillas HTML
│   ├── layout.html     # Plantilla base
│   ├── login.html      # Página de inicio de sesión
│   ├── register.html   # Página de registro
│   ├── updater.html    # Página para editar tareas
│   └── dashboard.html  # Panel principal
```

## ⚙️ Funcionalidades

- Registro de usuarios
- Inicio de sesión
- Creación de tareas
- Visualización de tareas
- Edición de tareas
- Eliminación de tareas

## 🚀 Cómo Ejecutar el Proyecto

1. Clona el repositorio:
```bash
git clone [URL-del-repositorio]
```

2. Instala las dependencias:
```bash
pip install flask flask-login, mysql-connector
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre tu navegador y visita:
```
http://localhost:5000
```

## 💡 Notas Importantes

- Este proyecto está diseñado para ejecutarse localmente
- El enfoque principal está en la lógica backend y las operaciones con la base de datos
- La interfaz visual es básica y funcional, priorizando la demostración de la funcionalidad
- No es necesario utilizar Docker o utilizan entornos virtuales para mantener la simplicidad del proyecto

## 🔍 Características del Backend

- Consultas SQL directas para mejor entendimiento del proceso
- Manejo de sesiones de usuario
- Validaciones básicas de datos
- Estructura modular de código