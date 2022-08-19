from categoria.models import Categoria
from django.db import models
from django.utils import timezone


class Filme(models.Model):
    nome = models.CharField(max_length=50)
    diretor = models.CharField(max_length=100)
    elenco = models.CharField(max_length=200)
    sinopse = models.TextField(max_length=800)
    data_estreia = models.DateField(default=timezone.now, verbose_name='Data lançamento')
    nota_media = models.FloatField(default=0, verbose_name='Nota Média')
    categoria_filme = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,  blank=True, null=True, verbose_name='Categoria') 
    imagem_filme = models.URLField(default=None, null=True)
    
    def __str__(self):
        return self.nome
    
    def __unicode__(self):
        return self.nome
