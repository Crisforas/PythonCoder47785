from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Curso


# Create your views here.
def mostar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "cris"
    }
    return render(request, "AppCoder/cursos.htmal", contexto)
def crear_curso(request):
    curso = Curso(nombre="Python", camada=47780)
    curso.save()
    contexto = {"curso": curso}

    return redeirect("/App/cursos")  #get


def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Luis"}
    return render(request, 'base.html', contexto)