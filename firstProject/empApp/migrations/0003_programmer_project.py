# Generated by Django 5.0.6 on 2024-06-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empApp", "0002_alter_employee_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Programmer",
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
                ("name", models.CharField(max_length=30)),
                ("salary", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=30)),
                ("programmers", models.ManyToManyField(to="empApp.programmer")),
            ],
        ),
    ]
