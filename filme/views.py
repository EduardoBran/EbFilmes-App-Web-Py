from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *


class FilmeIndex(ListView):
    model = Filme
    template_name = 'filme/index.html'
    context_object_name = 'allMovies'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('nome')
        return qs
