from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Category, Post


class CategoriesList(TemplateView):
    """
    Displays list of categories
    """
    template_name = "posts/categories.html"

    def get(self, request, *args, **kwargs):
        self.categories = Category.objects.all()
        return super(CategoriesList, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoriesList, self).get_context_data(**kwargs)
        context['categories'] = self.categories
        return context
