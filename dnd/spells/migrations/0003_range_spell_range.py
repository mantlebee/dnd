# Generated by Django 5.0.6 on 2024-07-04 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spells", "0002_spell_components_spell_duration"),
    ]

    operations = [
        migrations.CreateModel(
            name="Range",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="spell",
            name="range",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="spells.range",
            ),
            preserve_default=False,
        ),
    ]
