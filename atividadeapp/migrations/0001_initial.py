# Generated by Django 4.0.6 on 2023-03-28 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=50)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=50)),
                ('descricao', models.CharField(max_length=100)),
                ('categoria', models.ManyToManyField(related_name='bispo', to='atividadeapp.category')),
            ],
        ),
    ]
