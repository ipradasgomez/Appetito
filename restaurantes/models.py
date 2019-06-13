from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from math import *
import decimal

# Create your models here.
class Restaurante(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del Restaurante')
    descr = models.TextField(max_length=240, verbose_name='Descripción del restaurante')
    logo = models.ImageField(upload_to='uploaded_img/logos/', verbose_name='Logotipo')
    banner = models.ImageField(upload_to='uploaded_img/restaurants/', verbose_name='Foto de cabecera')
    telefono = models.IntegerField(verbose_name='Teléfono de contacto', blank=True, default=None, null=True)
    email = models.EmailField(max_length=15, verbose_name='Email de contacto',blank=True, default='')

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    direccion = models.CharField(max_length=100, verbose_name="Dirección", blank=False)
    lat = models.DecimalField(max_digits=11, decimal_places=7, default=0, verbose_name="Latitud", blank=False, null=False, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    long = models.DecimalField(max_digits=11, decimal_places=7, default=0, verbose_name="Longitud", blank=False, null=False, validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name="direcciones")

    def __str__(self):
        return self.direccion
    
    def en_radio(self, distance, center_lat, center_long):
        earth_r = decimal.Decimal(6371e3)
        pi=(22/7)
        pi=decimal.Decimal(pi)
        distance = decimal.Decimal(distance)
        center_lat= decimal.Decimal(center_lat)
        center_long= decimal.Decimal(center_long)
        
        center_lat_radian = center_lat*(pi/180)
        direc_lat_radian = self.lat*(pi/180)
        dif_lats = (self.lat-center_lat)*(pi/180)
        dif_longs = (self.long-center_long)*(pi/180)

        a = sin(dif_lats/2) *  sin(dif_lats/2) + cos(center_lat_radian) * cos(direc_lat_radian) * sin(dif_longs/2) * sin(dif_longs/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        c=decimal.Decimal(c)
        km = earth_r*c             
             
        return km < distance*1000