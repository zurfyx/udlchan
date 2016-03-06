from django.shortcuts import render
from django.views.generic import TemplateView


class CategoriesList(TemplateView):
    template_name = "posts/categories.html"
