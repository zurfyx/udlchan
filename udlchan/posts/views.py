from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Category, Post
from .forms import CategoryForm


class CategoryList(ListView):
    """
    Displays list of categories
    """
    model = Category
    template_name = 'posts/categories.html'


class CategoryAdd(CreateView):
    """
    Add category. Provides a form and handling to add a new category.
    """
    model = Category
    form_class = CategoryForm
    template_name = 'posts/categories_add.html'

    def get_success_url(self):
        return reverse('posts:categories')


class CategoryPostList(ListView):
    """
    Shows list of posts in a Category.
    """
    model = Post
    template_name = 'posts/category_posts.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category,
                                          title=self.kwargs['category'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class PostShow(DetailView):
    """
    Shows a specific post.
    """
    model = Post
    template_name = 'posts/'
