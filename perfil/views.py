from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('filmes:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # add message
                    return redirect('filmes:index')
                else:
                    return render(request, 'perfil/login.html', {"error": "Sua conta está desabilitada."})
            else:
                return render(request, 'perfil/login.html', {"error": "Usuário ou senha inválidos. Tente novamente."}) 
        else:
            return render(request, 'perfil/login.html')
        

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        # add message
        return redirect('filmes:index')
    else:
        # add message
        return redirect('filmes:index')


def registerPage(request):
    return render(request, 'perfil/register.html')
