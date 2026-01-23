from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios_app.models import Cliente

class ClienteCreateForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ["username", "email"]

class ClienteChangeForm(UserChangeForm):
    class Meta:
        model = Cliente
        fields = (
            "avatar",
            "fecha_de_nacimiento",
            "first_name",
            "last_name",
            "password",
        )

        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }