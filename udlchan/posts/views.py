from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView
from .models import Category, Post
from .forms import CategoryForm


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


class CategoriesAdd(CreateView):
    """
    Add category. Provides a form and handling to add a new category.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'posts/categories_add.html'

    def get_success_url(self):
        return reverse('posts:categories')
