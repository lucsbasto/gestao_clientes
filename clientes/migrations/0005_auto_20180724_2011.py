# Generated by Django 2.0.6 on 2018-07-24 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='descont',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='number',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='venda',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]