# Generated by Django 2.1.5 on 2019-06-20 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20190618_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_gramo',
            field=models.IntegerField(default=8000, verbose_name='Precio por gramo'),
        ),
    ]
