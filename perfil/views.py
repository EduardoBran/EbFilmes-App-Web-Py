from django.shortcuts import render


def loginPage(request):
    return render(request, 'perfil/login.html')


def registerPage(request):
    return render(request, 'perfil/register.html')
