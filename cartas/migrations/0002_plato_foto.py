# Generated by Django 2.2 on 2019-06-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='foto',
            field=models.ImageField(default=None, upload_to='uploaded_img/platos/', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]