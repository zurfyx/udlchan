from django.views.generic import TemplateView
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


class CategoriesAdd(TemplateView):
    """
    Add category. Provides a form and handling to add a new category.
    """
    form_class = CategoryForm
    template_name = "posts/categories_add.html"

    def get(self, request, *args, **kwargs):
        return super(CategoriesAdd, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoriesAdd, self).get_context_data(**kwargs)
        if 'form_add' not in context:
            context['form_add'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form, **kwargs)
        else:
            kwargs = self.form_invalid(form, **kwargs)

        return super(CategoriesAdd, self).get(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        # TODO save form
        # TODO redirect to list of categories
        pass

    def form_invalid(self, form, **kwargs):
        context = super(CategoriesAdd, self).get_context_data(**kwargs)
        context['form_add'] = form
        return context
