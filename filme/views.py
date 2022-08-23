from comentario.models import Comentario
from django.contrib import messages
from django.db.models import Avg, Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView

from .forms import *
from .models import *


class FilmeIndex(ListView):
    model = Filme
    template_name = 'filme/indexNome.html'
    context_object_name = 'allMovies'
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('nome')
        return qs

class FilmeIndexDataAntigo(FilmeIndex):
    template_name = 'filme/indexDataAntigo.html'
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('data_estreia')
        return qs

class FilmeIndexDataNovo(FilmeIndex):
    template_name = 'filme/indexDataNovo.html'
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-data_estreia')
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


class FilmeBusca(FilmeIndex):
    template_name = 'filme/filme_busca.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termo'] = self.request.GET.get('termo')
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        
        if not termo:
            return qs
        
        qs = qs.filter(
            Q(nome__icontains=termo) |
            Q(diretor__icontains=termo) |
            Q(elenco__icontains=termo)
        )
        
        return qs
    

def detailPage(request, movie_id):
    try:
        movie = Filme.objects.get(pk=movie_id)
    except:
        raise Http404('Filme não existe.')
    
    categorias = Categoria.objects.order_by('nome_cat')
    comentarios = Comentario.objects.filter(filme=movie_id)
    
    media = comentarios.aggregate(Avg('nota'))['nota__avg']
    # print(media)
    
    if media == None:
        media = 0
    
    media = round(media, 2)
        
    context = {
        'movie': movie,
        'categorias': categorias,
        'comentarios': comentarios,
        'media': media
    }
    return render(request, 'filme/filme_detalhes.html', context)


def sobreView(request):
    if str(request.method) == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            #chamando método de envio de email
            form.send_email()
            messages.success(request, 'Email enviado com sucesso.')
            form = ContatoForm()
        else:
            messages.error(request, 'Email NÃO FOI enviado com sucesso.')
    else:
        form = ContatoForm()

    categorias = Categoria.objects.order_by('nome_cat')
    context = {
        'form': form,
        'categorias': categorias
    }
    return render(request, 'filme/sobre.html', context)


def projetosView(request):
    categorias = Categoria.objects.order_by('nome_cat')
    
    context = {
        'categorias': categorias
    }
    return render(request, 'filme/projetos.html', context)
