# Generated by Django 2.1.2 on 2018-10-25 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_auto_20181016_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='tipovivienda',
            field=models.CharField(choices=[('Patio grande', 'Patio grande'), ('Patio pequeño', 'Patio pequeño'), ('Casa sin patio', 'Casa sin patio'), ('Departamento', 'Departamento')], max_length=20),
        ),
    ]
