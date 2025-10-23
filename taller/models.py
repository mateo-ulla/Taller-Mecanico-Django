from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Cotizacion(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    servicio_solicitado = models.CharField(max_length=255)
    detalles = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.servicio_solicitado}"

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
    
    TIPO_CHOICES = [
        ('producto', 'Producto'),
        ('servicio', 'Servicio'),
    ]
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField(default=0)
    fabricante = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='producto')

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
