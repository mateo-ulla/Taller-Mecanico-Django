from django.contrib import admin
from .models import Cliente, Mecanico, Producto, Proveedor, Usuario

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre','apellido','telefono')

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('legajo','nombre','apellido','rol','estado')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','precio','fabricante')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','cuit','telefono')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','usuario','nombre','apellido','rol')
