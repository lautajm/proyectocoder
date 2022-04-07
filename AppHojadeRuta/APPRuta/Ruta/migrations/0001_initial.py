# Generated by Django 4.0.3 on 2022-04-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('Cant_moviles', models.CharField(max_length=50, verbose_name='CantidadMovil')),
                ('Cant_pedidos', models.CharField(max_length=50, verbose_name='CantidadPedidos')),
                ('Contacto', models.CharField(max_length=50, verbose_name='NumerodeContacto')),
                ('pedido', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField()),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('Contacto', models.CharField(max_length=50, verbose_name='Contacto')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
            ],
        ),
        migrations.CreateModel(
            name='Hoja_de_Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField()),
                ('Estado', models.CharField(max_length=50, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Movil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('Tipo', models.IntegerField(verbose_name='Tipo')),
                ('Matricula', models.CharField(max_length=50, verbose_name='Matricula')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
            ],
        ),
    ]