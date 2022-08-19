from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import *


class FilmeIndex(ListView):
    model = Filme
    template_name = 'filme/index.html'
    context_object_name = 'allMovies'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('nome')
        return qs


class FilmeCategoria(FilmeIndex):
    template_name = 'filme/filme_categoria.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        categoria = self.kwargs.get('categoria', None)
        
        if not categoria:
            return qs
        
        qs = qs.filter(categoria_filme__nome_cat__iexact=categoria)
        
        return qs


def detailPage(request, movie_id):
    try:
        movie = Filme.objects.get(pk=movie_id)
    except:
        raise Http404('Filme não existe.')
    
    context = {
        'movie': movie
    }
    return render(request, 'filme/detail.html', context)
