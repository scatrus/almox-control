# Generated by Django 3.0.5 on 2020-04-23 23:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_auto_20200415_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='notaempenho',
            name='data',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notaempenho',
            name='ne',
            field=models.CharField(default=3, max_length=16, verbose_name='NE'),
            preserve_default=False,
        ),
    ]
