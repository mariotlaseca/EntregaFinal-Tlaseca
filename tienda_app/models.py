from django.db import models

class Productos(models.Model):
    
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField(null=True)
    categoria = models.CharField(max_length=30)
    id = models.IntegerField(
        auto_created=True,
        unique=True,
        primary_key=True,
    )
    fecha_de_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Nombre: {self.nombre} Precio: {self.precio}"
    
