from django.urls import path

from . import views

app_name = 'comentario'

urlpatterns = [
    path('addComentario/<int:movie_id>/', views.addComentario, name='addComentario'),
    path('editComentario/<int:movie_id>/<int:comentario_id>', views.editComentario, name='editComentario'),
    path('deleteComentario/<int:movie_id>/<int:comentario_id>', views.deleteComentario, name='deleteComentario'),
    
]
