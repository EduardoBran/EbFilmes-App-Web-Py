from django.contrib import admin

from .models import *


class FilmeAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'diretor',
        'categoria_filme',
        'nota_media'
    ]
    search_fields = [
        'nome',
        'diretor',
        'elenco'
    ]
    list_editable = [
        'categoria_filme'
    ]


admin.site.register(Filme, FilmeAdmin)
