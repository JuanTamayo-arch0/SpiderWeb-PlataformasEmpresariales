# 🕸️ Foro Spider Web - Proyecto Django

Este es un foro estilo 4chan desarrollado con Django. Permite crear boards, publicar mensajes, responder, gestionar roles de usuario y moderar contenido.

## 🚀 Funcionalidades principales

- Creación y visualización de boards
- Publicación de posts con texto e imagen
- Sistema de respuestas (replies) colapsables
- Roles de usuario: `Usuario`, `Admin_foro`, `Admin_elementos`
- Autenticación, edición de perfil y subida de avatar
- Panel de administración para gestionar contenido
- Monitoreo con LogRocket (opcional)

---

## 🧰 Requisitos

- Python 3.9 o superior
- pip
- Git
- Virtualenv (opcional pero recomendado)
- PostgreSQL o SQLite (por defecto)

---

## ⚙️ Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. **Crea y activa un entorno virtual (opcional pero recomendado):**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. **Instala las dependencias:**

```bash
pip install django
```

4. **Aplica las migraciones:**

```bash
python manage.py migrate
```

5. **Inicia el servidor:**

```bash
python manage.py runserver
```