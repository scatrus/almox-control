# Generated by Django 3.0.5 on 2020-04-16 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_auto_20200415_0522'),
    ]

    operations = [
        migrations.AddField(
            model_name='notaempenho',
            name='ne',
            field=models.CharField(default=0, max_length=12, verbose_name='NE'),
            preserve_default=False,
        ),
    ]
