from django.urls import path
from . import views

urlpatterns = [
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
