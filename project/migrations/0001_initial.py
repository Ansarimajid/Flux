# Generated by Django 4.2.6 on 2024-03-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="projectPageSEO",
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
                ("meta_title", models.CharField(blank=True, max_length=500, null=True)),
                (
                    "meta_description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
            ],
        ),
    ]
