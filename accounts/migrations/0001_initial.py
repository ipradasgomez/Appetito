# Generated by Django 2.2.2 on 2019-06-06 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plans', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurantes', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='plans.Plan')),
                ('restaurante', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurante', to='restaurantes.Restaurante')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
