# Generated by Django 2.1.5 on 2019-09-21 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190921_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='numero_cel',
            new_name='celular',
        ),
    ]
