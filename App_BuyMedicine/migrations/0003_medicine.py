# Generated by Django 5.0.2 on 2024-02-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App_BuyMedicine", "0002_remove_prescription_doctor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Medicine",
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
                ("name", models.CharField(max_length=255)),
                ("needed", models.DecimalField(decimal_places=2, max_digits=10)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
