# Generated by Django 4.2 on 2023-05-02 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtx', '0011_auto_20230501_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodesetup',
            name='nodeId',
        ),
        migrations.AddField(
            model_name='nodesetup',
            name='limiarMedia',
            field=models.DecimalField(decimal_places=3, default=5, max_digits=12, verbose_name='limiar para media %'),
        ),
        migrations.AddField(
            model_name='nodesetup',
            name='limiarPico',
            field=models.DecimalField(decimal_places=3, default=10, max_digits=12, verbose_name='limiar para pico %'),
        ),
        migrations.AlterField(
            model_name='nodesetup',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vtx.node', unique=True),
        ),
    ]
