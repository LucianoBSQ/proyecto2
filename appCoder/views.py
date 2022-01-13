from django.shortcuts import render
from django.http import HttpResponse

from appCoder.models import Curso, Estudiante

# Create your views here.
def crea_curso(self, nombre, camada):
    curso = Curso(nombre = nombre, camada = camada)
    
    curso.save()

    return HttpResponse(f'Se creo el curso de {curso.nombre} con el numero de camada: {curso.camada}')

def sumar_estudiante(self,nombre,apellido,email):
    estudiante = Estudiante(nombre = nombre, apellido = apellido, email = email)

    estudiante.save()

    return HttpResponse (f'Se salvo el dato')

def sumar_profesor(self,nombre,apellido,email):
    profesor = Estudiante(nombre = nombre, apellido = apellido, email = email)

    profesor.save()

    return HttpResponse (f'Se salvo el dato')

