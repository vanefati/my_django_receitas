# Generated by Django 3.0.7 on 2020-06-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo_de_culinaria', models.CharField(max_length=200)),
                ('tempo_de_preparo', models.IntegerField()),
                ('quantidade_ingredientes', models.CharField(max_length=200)),
                ('modo_de_preparo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'receitas',
            },
        ),
    ]