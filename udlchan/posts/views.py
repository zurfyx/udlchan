from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView
from .models import Category, Post
from .forms import CategoryForm


class CategoriesList(ListView):
    """
    Displays list of categories
    """
    model = Category
    template_name = "posts/categories.html"


class CategoriesAdd(CreateView):
    """
    Add category. Provides a form and handling to add a new category.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'posts  /categories_add.html'

    def get_success_url(self):
        return reverse('posts:categories')
