# Proyecto Blog
Proyecto para crear publiaciones utilizando Django. Tiene las funciones de crear una publicación, eliminar, editar y listar las publicaciones de todos los usuarios. Solo se pueden editar/eliminar las publicaciones propias. 
Hay que crear un perfil ya que implementa autenticación de usuarios y hace uso de un middleware personalizado.

## Funcionalidades
- Crear, leer, actualizar y eliminar publicaciones.
- Autenticación de usuarios.
- Middleware para registrar solicitudes HTTP.

## Instalación

1. Clonar el repositorio.
[git clone https://github.com/Axell505/TP2.git](https://github.com/Axell505/TP3.git)

2. Crear y activar el entorno virtual.
 Dentro de la carpeta que se creará el Entorno Virtual: python -m venv env
 Para activarlo:
 Linux: source env/bin/activate
 En Windows: env\Scripts\activate

4. Instalar las dependencias.
pip install -r requirements.txt

5. Aplicar las migraciones de la base de datos.
python manage.py migrate

6. Correr el servidor.
python manage.py runserver

## Uso
Accede a la aplicación desde el navegador usando: http://localhost:8000/ o http://127.0.0.1:8000/
Crear un usuario o iniciar sesión (si es que ya se creó uno antes). 

## Requisitos
Python 3.12.5 Django 4.2 y SQLlite (u otra base de datos compatible)
