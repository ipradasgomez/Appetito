# Generated by Django 2.2 on 2019-04-17 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='plan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.Plan'),
        ),
    ]