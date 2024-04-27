# Generated by Django 5.0.4 on 2024-04-18 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Ingresa tu nombre')),
                ('email', models.EmailField(max_length=20, verbose_name='Escribe tu email')),
                ('message', models.TextField(max_length=100, verbose_name='Escribe tu mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contactos',
                'ordering': ['-created'],
            },
        ),
    ]