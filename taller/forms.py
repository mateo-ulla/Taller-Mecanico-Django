from django import forms
from .models import Cliente, Mecanico, Producto, Proveedor, Usuario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {f.name: forms.TextInput(attrs={'class':'form-control'}) for f in model._meta.fields}

class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = '__all__'
        widgets = {f.name: forms.TextInput(attrs={'class':'form-control'}) for f in model._meta.fields}

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'fabricante': forms.TextInput(attrs={'class':'form-control'}),
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {f.name: forms.TextInput(attrs={'class':'form-control'}) for f in model._meta.fields}

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {f.name: forms.TextInput(attrs={'class':'form-control'}) for f in model._meta.fields}
