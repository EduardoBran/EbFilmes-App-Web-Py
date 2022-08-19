# Generated by Django 4.1 on 2022-08-19 15:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('diretor', models.CharField(max_length=100)),
                ('elenco', models.CharField(max_length=200)),
                ('sinopse', models.TextField(max_length=800)),
                ('data_estreia', models.DateField(default=django.utils.timezone.now, verbose_name='Data lançamento')),
                ('nota_media', models.FloatField(default=0, verbose_name='Nota Média')),
                ('imagem_filme', models.URLField(default=None, null=True)),
                ('categoria_filme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categoria.categoria', verbose_name='Categoria')),
            ],
        ),
    ]