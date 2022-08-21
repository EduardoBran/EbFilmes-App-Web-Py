from django.urls import path

from . import views

app_name = 'comentario'

urlpatterns = [
    path('addComentario/<int:movie_id>/', views.addComentario, name='addComentario')
]
