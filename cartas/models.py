from django.db import models
from restaurantes.models import Restaurante, Direccion
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Título de la categoría')
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name="categorias")

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del plato')
    lista_ingredientes = models.TextField(max_length=240, verbose_name='Lista de ingredientes', blank=True)
    descripcion = models.TextField(max_length=240, verbose_name='Descripción')
    precio = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="Precio", blank=False, null=False, validators=[MinValueValidator(0)])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="platos")
    foto = models.ImageField(upload_to='uploaded_img/platos/', verbose_name='Imagen')

    def __str__(self):
        return self.nombre



class Tag(models.Model):
    tagtext = models.CharField(max_length=30, verbose_name='Tag', blank=False, null=False, default='')
    plato = models.ManyToManyField(Plato, related_name="tags")

    def __str__(self):
        return self.tagtext