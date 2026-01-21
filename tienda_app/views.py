from django.shortcuts import render, redirect, get_object_or_404
from tienda_app.models import Productos
from tienda_app.forms import ProductosForm

def home(request):
    return render(request, "tienda_app/index.html")

def listar_productos(request):
    nombre = request.GET.get("nombre")
    productos_query = Productos.objects.all()
    if nombre:
        productos_query = Productos.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "productos": productos_query
    }
    return render(request, "tienda_app/productos.html", contexto)

def crear_producto(request):
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_productos")
    else:
        form = ProductosForm()
    
    return render(request, 'tienda_app/crear_producto.html', {'form':form})

def ver_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    contexto = {
        "producto":producto
    }

    return render(request, 'tienda_app/ver_producto.html', contexto)

def mostrar_productos(request):
    nombre = request.GET.get("nombre")
    productos_query = Productos.objects.all()
    if nombre:
        productos_query = Productos.objects.filter(
            nombre__icontains=nombre
        )
    contexto = {
        "productos": productos_query
    }
    return render(request, "tienda_app/tienda.html", contexto)