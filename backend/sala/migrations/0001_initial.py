# Generated by Django 3.0.4 on 2022-02-28 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Ferramentas',
                'db_table': 'Ferramenta',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ferramentas', models.ManyToManyField(blank=True, to='sala.Ferramenta')),
            ],
            options={
                'verbose_name_plural': 'Tipos',
                'db_table': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('abreviatura', models.CharField(blank=True, max_length=25, null=True)),
                ('capacidade', models.IntegerField()),
                ('tipos', models.ManyToManyField(blank=True, to='sala.Tipo')),
            ],
            options={
                'verbose_name_plural': 'Salas',
                'db_table': 'Sala',
            },
        ),
    ]
