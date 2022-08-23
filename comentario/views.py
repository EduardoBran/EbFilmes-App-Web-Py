from django.contrib import messages
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
                
                if len(data.comentario) < 5:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        f"Comentário NÃO foi adicionado. O comentário deve ter no mínimo 5 caracteres."
                    )
                    return redirect('filmes:detail', movie_id)     
                
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f"Comentário enviado com sucesso."
                )
                return redirect('filmes:detail', movie_id)
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f"Comentário NÃO foi adicionado."
                )
                return redirect('filmes:detail', movie_id)
        else:
            form = ComentarioForm()
        
        context = {'form': form}
        return render(request, 'filme/filme_detalhes.html', context)
    else:
        return redirect('perfil:login')    


def editComentario(request, movie_id, comentario_id):
    if request.user.is_authenticated:
        user_comentario = Comentario.objects.get(filme=movie_id, pk=comentario_id)
        
        if request.user == user_comentario.user:
            if request.method == 'POST':
                form = ComentarioForm(request.POST or None, instance=user_comentario)
                
                if form.is_valid():
                    data = form.save(commit=False)
                    
                    if (data.nota > 10) or (data.nota < 0):
                        error = 'Valor de nota inválido. Favor escolher entre 0 e 10.'
                        context = {
                            'error': error,
                            'form': form
                        }
                        messages.add_message(
                            request,
                            messages.ERROR,
                            f"Não foi possível salvar o comentário editado."
                        )
                        return render(request, 'comentario/editComentario.html', context)
                    else:
                        data.save()
                        messages.add_message(
                            request,
                            messages.SUCCESS,
                            f"Comentáro foi editado com sucesso."
                        )
                        return redirect('filmes:detail', movie_id)                        
            else:
                form = ComentarioForm(instance=user_comentario)
            
            context = {'form': form}
            return render(request, 'comentario/editComentario.html', context)
        else:
            return redirect('filmes:detail', movie_id)
    else:                
        return redirect('perfil:login')
    

def deleteComentario(request, movie_id, comentario_id):
    if request.user.is_authenticated:
        comentario = Comentario.objects.get(filme=movie_id, pk=comentario_id)
        
        if request.user == comentario.user:
            comentario.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Comentáro foi excluído com sucesso."
            )
        else:
            return redirect('filmes:detail', movie_id)
    return redirect('filmes:detail', movie_id)
