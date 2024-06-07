# Generated by Django 5.0.6 on 2024-06-04 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
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
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("name", models.CharField(max_length=30)),
                ("assingedTo", models.CharField(max_length=30)),
                ("priority", models.IntegerField()),
            ],
        ),
    ]
