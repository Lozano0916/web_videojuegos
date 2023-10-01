"""
URL configuration for videojuegos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path
from videojuegos.views import bienvenida
from videojuegos.views import inicio,catalogo,producto

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/',bienvenida),
    path('inicio/',inicio, name='inicio'),
    path('catalogo/',catalogo, name='catalogo'),
    path('producto/',producto, name='producto'),
    path('', views.inicio),
]
# En urls.py


def health_check(request):
    # Agrega aquí cualquier lógica de verificación de estado necesaria
    return HttpResponse(status=200)

urlpatterns = [
    # ... otras rutas de tu aplicación ...
    path('healthcheck/', health_check, name='health_check'),
]

