# Generated by Django 3.2.3 on 2021-06-01 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alimentos', '0003_reservacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservacion',
            name='created',
        ),
    ]
