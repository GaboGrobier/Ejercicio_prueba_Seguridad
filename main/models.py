from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=150, unique=True)  # Nuevo campo
    password = models.CharField(max_length=128, null=True)  # Hacerlo nullable inicialmente

    def __str__(self):
        return self.nombre
