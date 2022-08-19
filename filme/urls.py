from django.urls import path

from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.FilmeIndex.as_view(), name='index'),
    path('<int:movie_id>/', views.detailPage, name='detail'),
    path('categoria/<str:categoria>', views.FilmeCategoria.as_view(), name='categoria'),
]
