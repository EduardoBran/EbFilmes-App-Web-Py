from django.contrib import admin

from .models import *


class ComentarioAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'filme',
        'nota',
    ]
    search_fields = [
        'filme',
        'user'
    ]

admin.site.register(Comentario, ComentarioAdmin)
