# Generated by Django 4.2.1 on 2023-05-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("locadora", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id_categoria",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=255)),
            ],
        ),
    ]
