# Generated by Django 4.2 on 2023-04-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtx', '0003_node_alerta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='estado',
            field=models.CharField(choices=[('ok', 'Ok'), ('falha', 'Falha'), ('alerta', 'Alerta'), ('Indefinido', 'Desconhecido')], default='Indefinido', max_length=30, verbose_name='Estado'),
        ),
    ]