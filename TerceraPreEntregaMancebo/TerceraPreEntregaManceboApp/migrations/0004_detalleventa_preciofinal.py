# Generated by Django 4.2.2 on 2023-07-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TerceraPreEntregaManceboApp', '0003_remove_venta_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='precioFinal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
