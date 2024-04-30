# Generated by Django 5.0.4 on 2024-04-30 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trabajos", "0004_employee_experience"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="../static/i")),
                (
                    "github_link",
                    models.URLField(default="https://github.com/Mgobeaalcoba"),
                ),
                ("github_link_img", models.ImageField(upload_to="../static/i")),
            ],
        ),
    ]