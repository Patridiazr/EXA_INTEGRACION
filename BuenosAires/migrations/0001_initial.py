# Generated by Django 2.2.2 on 2019-06-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='ProduI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('direccion', models.CharField(default='default', max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.CharField(max_length=100)),
                ('estado', models.CharField(default='Pendiente', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=100)),
            ],
        ),
    ]
