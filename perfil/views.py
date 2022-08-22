from categoria.models import Categoria
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import RegistrationForm


def loginPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            'Você já se encontra logado.'
        )
        return redirect('filmes:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(
                    request,
                    messages.SUCCESS,
                    f"Bem vindo(a) {username}, você agora está logado e pode dar nota(s) e escrever comentário(s)."
                )
                    return redirect('filmes:index')
                else: 
                    return render(request, 'perfil/login.html', {"error": "Sua conta está desabilitada."})
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Usuário ou senha estão inválidos.'             
                )
                return render(request, 'perfil/login.html') 
        else:
            categorias = Categoria.objects.order_by('nome_cat')
            context = {'categorias': categorias}
            return render(request, 'perfil/login.html', context)
        

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            f'Usuário foi deslogado com sucesso.'
        )
        return redirect('filmes:index')
    else:
        messages.add_message(
            request,
            messages.WARNING,
            f'Você já está deslogado.'
        )
        return redirect('filmes:index')


def registerPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            f'Você já se encontra logado.'
        )
        return redirect('filmes:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            form = RegistrationForm(request.POST or None)
            
            if form.is_valid():
                user = form.save()
                
                raw_password = form.cleaned_data.get('password1')
                
                user = authenticate(username=user.username, password=raw_password)
                
                if user is not None:
                    login(request, user)
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Bem vindo(a) {username}, você agora está cadastrado e pode dar nota(s) e escrever comentário(s)."
                    )
                    return redirect('filmes:index')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... você digitou algum campo inválido.'
                )
        else:
            form = RegistrationForm()
        
        categorias = Categoria.objects.order_by('nome_cat')    
        context = {
            'form': form,
            'categorias': categorias
        }
        return render(request, 'perfil/register.html', context)
