from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni})"

class Mecanico(models.Model):
    legajo = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    rol = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.legajo}"

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    fabricante = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255, unique=True)
    contrasena = models.CharField(max_length=255)
    rol = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.usuario
