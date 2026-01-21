from django.urls import path
from tienda_app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("listar_productos", listar_productos, name="listar_productos"),
    path("mostrar_productos", mostrar_productos, name="mostrar_productos"),
    path("crear_producto", crear_producto, name="crear_producto"),
    path("ver_producto/<int:id>/", ver_producto, name="ver_producto"),
]
