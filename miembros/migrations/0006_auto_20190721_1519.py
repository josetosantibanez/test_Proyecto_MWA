# Generated by Django 2.1.5 on 2019-07-21 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '0005_auto_20190619_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembro',
            name='fotocopia_carnet_a',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='fotocopia_carnet_b',
        ),
        migrations.RemoveField(
            model_name='miembro',
            name='receta',
        ),
    ]
