# Generated by Django 5.0.6 on 2024-06-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_persona_donador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='donador',
            field=models.BooleanField(default=True),
        ),
    ]
