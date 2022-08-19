from django.shortcuts import render
from django.views.generic import TemplateView


class FilmeIndex(TemplateView):
    template_name = 'filme/index.html'
