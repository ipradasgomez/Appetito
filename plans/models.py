from django.db import models
import math
# Create your models here.
class Plan(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre del plan')
    max_empresas = models.IntegerField(default=0, verbose_name='Max de empresas (0 = infinito)')
    max_categorias = models.IntegerField(default=1, verbose_name='Max categorías por empresa (0 = infinito)')
    max_productos_x_cat = models.IntegerField(default=5, verbose_name='Max productos por categoría (0 = infinito)')
    max_tags_x_prod = models.IntegerField(default=3, verbose_name='Max tag x producto (0= infinito)')
    permite_anuncios = models.BooleanField(default=False, verbose_name='Permitir crear anuncios')
    precio = models.DecimalField(decimal_places=2, max_digits=6, default=0.0)
    class_descr = models.CharField(max_length = 10, default="free" , verbose_name='Clase CSS Descriptiva')
    recomendado = models.BooleanField(default="False", verbose_name='Mostrar como recomendado')
    recomendado_text = models.CharField(max_length=50, null=True, blank=True, verbose_name='Texto de recomendación')

    def __str__(self):
        return "{}".format(self.nombre).upper()

    def precio_pentera(self):
        return str(self.precio).split(".")[0]

    def precio_pdecimal(self):
        res = str(float(self.precio - math.floor(self.precio)))
        return res.split(".")[1]

    class Meta:
        verbose_name="Plan"
        verbose_name_plural = "Planes"