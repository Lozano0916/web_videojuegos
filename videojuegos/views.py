from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect

def bienvenida(request):
    return HttpResponse("Bienvenido a este curso de django")

def inicio(request):
    # Abre y lee el archivo HTML con la codificación 'utf-8'
    with open('C:/ProyectosDjango/videojuegos/videojuegos/plantillas/index.html', 'r', encoding='utf-8') as inicioweb:
        contenido_html = inicioweb.read()
    # Crea una instancia de la clase Template de Django
    template = Template(contenido_html)
    # Crea un contexto (puede estar vacío o puedes agregar datos)
    contexto = Context()
    # Renderiza el template con el contexto
    documento = template.render(contexto)

    return HttpResponse(documento)

def catalogo(request):
    # Abre y lee el archivo HTML con la codificación 'utf-8'
    with open('C:/ProyectosDjango/videojuegos/videojuegos/plantillas/Catalogo.html', 'r', encoding='utf-8') as catalogo:
        contenido_html = catalogo.read()
    # Crea una instancia de la clase Template de Django
    template = Template(contenido_html)
    # Crea un contexto (puede estar vacío o puedes agregar datos)
    contexto = Context()
    # Renderiza el template con el contexto
    documento = template.render(contexto)

    return HttpResponse(documento)
def producto(request):
    # Abre y lee el archivo HTML con la codificación 'utf-8'
    with open('C:/ProyectosDjango/videojuegos/videojuegos/plantillas/producto.html', 'r', encoding='utf-8') as catalogo:
        contenido_html = catalogo.read()
    # Crea una instancia de la clase Template de Django
    template = Template(contenido_html)
    # Crea un contexto (puede estar vacío o puedes agregar datos)
    contexto = Context()
    # Renderiza el template con el contexto
    documento = template.render(contexto)

    return HttpResponse(documento)


