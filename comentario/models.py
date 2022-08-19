from django.contrib.auth.models import User
from django.db import models
from filme.models import Filme


class Comentario(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    comentario = models.TextField(max_length=1000, verbose_name='Comentário')
    nota = models.FloatField(default=0)
    
    def __str__(self):
        return self.user.username
