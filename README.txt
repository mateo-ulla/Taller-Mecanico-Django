Taller Mecánico - Proyecto Django
================================

Instrucciones para Windows (PowerShell):

1) Crear entorno virtual:
   python -m venv .venv
   .venv\Scripts\activate

2) Instalar dependencias:
   pip install -r requirements.txt

3) Crear base de datos MySQL (desde consola MySQL):
   mysql -u root -p
   CREATE DATABASE taller_mecanico CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   exit

4) Importar script SQL proporcionado (opcional si querés datos iniciales):
   mysql -u root -p taller_mecanico < taller_mecanico.sql

5) Ejecutar migraciones y levantar servidor:
   python manage.py migrate
   python manage.py runserver

Nota:
- Este proyecto usa PyMySQL (configurado en taller_project/__init__.py).
- El proyecto crea un superusuario "admin" con contraseña "1234" automáticamente la primera vez que se ejecuta el servidor tras migraciones.
