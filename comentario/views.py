from django.shortcuts import redirect, render
from filme.models import Filme

from .forms import *
from .models import *


def addComentario(request, movie_id):
    if request.user.is_authenticated:
        movie = Filme.objects.get(pk=movie_id)
        
        if request.method == 'POST':
            form = ComentarioForm(request.POST or None)
            
            if form.is_valid():
                data = form.save(commit=False)
                data.comentario = request.POST['comentario']
                data.nota = request.POST['nota']
                data.user = request.user
                data.filme = movie
                data.save()
                
                return redirect('filmes:detail', movie_id)
        else:
            form = ComentarioForm()
        
        context = {'form': form}
        return render(request, 'filme/filme_detalhes.html', context)
    else:
        return redirect('perfil:login')    
