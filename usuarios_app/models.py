from django.db import models
from django.contrib.auth.models import AbstractUser

def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"

class Cliente(AbstractUser):

    avatar = models.ImageField(
        upload_to= avatar_upload_to,
        default="default/default.png",
        blank= True,
        null= True,
        verbose_name= "Avatar"
    )
    fecha_de_nacimiento = models.DateField(
        null= True,
        blank= True,
    )

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    
    def __str__(self):
        return f"{self.username}: {self.first_name}, {self.last_name}"
