# Generated by Django 4.2.14 on 2024-08-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Developer",
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
                ("lid", models.CharField(max_length=20)),
                ("dname", models.CharField(max_length=100)),
                ("demail", models.EmailField(max_length=254)),
                ("contact", models.CharField(max_length=10)),
            ],
            options={"db_table": "developer",},
        ),
    ]
