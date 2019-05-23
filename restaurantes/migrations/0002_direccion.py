# Generated by Django 2.2 on 2019-05-07 18:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('lat', models.DecimalField(decimal_places=7, default=0, max_digits=11, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Latitud')),
                ('long', models.DecimalField(decimal_places=7, default=0, max_digits=11, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Longitud')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='restaurantes.Restaurante')),
            ],
        ),
    ]