# Generated by Django 5.0.6 on 2024-05-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(),
        ),
    ]