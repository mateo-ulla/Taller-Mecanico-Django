from django.urls import path
from . import views

app_name = 'taller'
urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página pública
    path('acerca/', views.acerca, name='acerca'),
    path('servicios/', views.servicios, name='servicios'),

    path('ubic_contacto/', views.ubic_contacto, name='ubic_contacto'),
    path('contacto/', views.contacto, name='contacto'),
    path('cotizacion/', views.cotizacion, name='cotizacion'),


    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/<str:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('clientes/<str:pk>/delete/', views.cliente_delete, name='cliente_delete'),

    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/nuevo/', views.proveedor_create, name='proveedor_create'),

    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),

    path('mecanicos/', views.mecanico_list, name='mecanico_list'),
    path('mecanicos/nuevo/', views.mecanico_create, name='mecanico_create'),

    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/nuevo/', views.usuario_create, name='usuario_create'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
