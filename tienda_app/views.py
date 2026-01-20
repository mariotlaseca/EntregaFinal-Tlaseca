from django.shortcuts import render
from tienda_app.models import Productos

def home(request):
    return render(request, "tienda_app/index.html")

def listar_productos(request):
    productos_query = Productos.objects.all()
    contexto = {
        "productos": productos_query
    }
    return render(request, "tienda_app/productos.html", contexto)

