# Generated by Django 5.0.4 on 2024-05-01 00:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("precios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paquete",
            name="precio",
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
