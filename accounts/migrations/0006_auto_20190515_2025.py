# Generated by Django 2.2 on 2019-05-15 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_restaurante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='restaurante',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurante', to='restaurantes.Restaurante'),
        ),
    ]