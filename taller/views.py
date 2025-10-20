from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Mecanico, Producto, Proveedor, Usuario
from .forms import ClienteForm, MecanicoForm, ProductoForm, ProveedorForm, UsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('taller:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'taller/login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('taller:login')

def dashboard(request):
    resumen = {
        'clientes': Cliente.objects.count(),
        'proveedores': Proveedor.objects.count(),
        'productos': Producto.objects.count(),
        'empleados': Mecanico.objects.count(),
        'usuarios': Usuario.objects.count(),
    }
    return render(request, 'taller/dashboard.html', {'resumen': resumen})

# Generic list/create/edit/delete for Cliente as example; others follow same pattern
def cliente_list(request):
    clientes = Cliente.objects.all().order_by('apellido')
    return render(request, 'taller/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado')
            return redirect('taller:cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'taller/cliente_form.html', {'form': form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado')
            return redirect('taller:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'taller/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado')
        return redirect('taller:cliente_list')
    return render(request, 'taller/confirm_delete.html', {'obj': cliente})

# For remaining models, minimal CRUD
def proveedor_list(request):
    return render(request, 'taller/proveedor_list.html', {'proveedores': Proveedor.objects.all()})

def proveedor_create(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taller:proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'taller/proveedor_form.html', {'form': form})

def producto_list(request):
    return render(request, 'taller/producto_list.html', {'productos': Producto.objects.all()})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taller:producto_list')
    else:
        form = ProductoForm()
    return render(request, 'taller/producto_form.html', {'form': form})

def mecanico_list(request):
    return render(request, 'taller/mecanico_list.html', {'mecanicos': Mecanico.objects.all()})

def mecanico_create(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taller:mecanico_list')
    else:
        form = MecanicoForm()
    return render(request, 'taller/mecanico_form.html', {'form': form})

def usuario_list(request):
    return render(request, 'taller/usuario_list.html', {'usuarios': Usuario.objects.all()})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taller:usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'taller/usuario_form.html', {'form': form})
