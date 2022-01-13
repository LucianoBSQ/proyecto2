from django.db import models

# Create your models here.

class Curso(models.Model): #Herencia de la clase Model, clase generica de django

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    email = models.EmailField('email', max_length=254)

class Profesor(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    email = models.EmailField('email', max_length=254,default='0000000')


    