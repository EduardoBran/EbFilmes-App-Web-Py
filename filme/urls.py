from django.urls import path

from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.FilmeIndex.as_view(), name='index'),
    path('ord_data_antigo/', views.FilmeIndexDataAntigo.as_view(), name='index_data_antigo'),
    path('ord_data_novo/', views.FilmeIndexDataNovo.as_view(), name='index_data_novo'),
    path('<int:movie_id>/', views.detailPage, name='detail'),
    path('categoria/<str:categoria>', views.FilmeCategoria.as_view(), name='categoria'),
    path('busca/', views.FilmeBusca.as_view(), name='busca'),
]
