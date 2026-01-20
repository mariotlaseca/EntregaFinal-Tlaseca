from django.urls import path
from tienda_app.views import *

urlpatterns = [
    path("", home, name="home"),
    path("listar_productos", listar_productos, name="listar_productos"),
]
