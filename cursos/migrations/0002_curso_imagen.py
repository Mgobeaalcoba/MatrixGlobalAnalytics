# Generated by Django 5.0.4 on 2024-05-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cursos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="imagen",
            field=models.CharField(
                default="../../../static/i/logo.jpg", max_length=200
            ),
        ),
    ]