# Generated by Django 4.0.3 on 2022-04-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ruta', '0003_alter_base_estado_alter_movil_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nro_de_cliente',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]