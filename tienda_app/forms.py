from django import forms
from tienda_app.models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            "imagen",
            "nombre",
            "descripcion",
            "precio",
            "categoria",
        ]
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'precio':forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria':forms.TextInput(attrs={'class': 'form-control'}),
        }