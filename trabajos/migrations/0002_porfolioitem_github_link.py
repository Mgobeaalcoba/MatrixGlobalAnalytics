# Generated by Django 5.0.4 on 2024-04-30 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trabajos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="porfolioitem",
            name="github_link",
            field=models.URLField(default="https://github.com/Mgobeaalcoba"),
        ),
    ]
