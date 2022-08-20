from django.urls import path

from . import views

app_name = 'perfil'

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
]
