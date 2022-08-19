from django.urls import path

from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.FilmeIndex.as_view(), name='index'),
]