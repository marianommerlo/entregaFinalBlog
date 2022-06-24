from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    descripcion= models.CharField(max_length=500)
    web= models.URLField()
    
    def __str__(self):
        return self.nombre +" "+ self.apellido