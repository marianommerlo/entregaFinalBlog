from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    descripcion= models.CharField(max_length=500)
    web= models.URLField()
    avatar= models.ImageField(upload_to= 'avatar/', blank= True)

#class Avatar(models.Model):
#    user= models.ForeignKey(User, on_delete=models.CASCADE)
#    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)
#Averiguar si con ImageField se puede deployear en heroku