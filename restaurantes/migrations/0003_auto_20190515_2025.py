# Generated by Django 2.2 on 2019-05-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0002_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurante',
            name='banner',
            field=models.ImageField(upload_to='uploaded_img/restaurants/', verbose_name='Foto de cabecera'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='descr',
            field=models.TextField(max_length=240, verbose_name='Descripción del restaurante'),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='logo',
            field=models.ImageField(upload_to='uploaded_img/logos/', verbose_name='Logotipo'),
        ),
    ]