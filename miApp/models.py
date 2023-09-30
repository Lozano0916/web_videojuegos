from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=200)
    creador = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ano_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)
    juego_f = models.CharField(max_length=100)
    comentario = models.CharField(max_length=200,default='')
    tiempo = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Plataformas(models.Model):
    nombre = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    ano_lanzamiento = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre