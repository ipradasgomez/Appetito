# Generated by Django 2.2 on 2019-06-08 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartas', '0002_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='restaurante',
            new_name='plato',
        ),
    ]