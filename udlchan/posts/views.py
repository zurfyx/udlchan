from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, View
from .models import Category, Post
from .forms import CategoryForm
from .utils import PostSorter


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
        return reverse('posts:category')


class CategoryPostList(ListView):
    """
    Shows list of posts in a Category.
    """
    model = Post
    template_name = 'posts/category_topics.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category,
                                          title=self.kwargs['category'])
        return Post.objects.filter(category=self.category, main=None)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TopicShow(ListView):
    """
    Shows a specific topic, a main post + its descendant posts
    """
    model = Post
    template_name = 'posts/topic.html'

    def get_queryset(self):
        self.main_post = get_object_or_404(Post, id=self.kwargs['post'],
                                           main=None, parent=None)
        queryset = Post.objects.filter(category=self.main_post.category,
                                   main=self.main_post)
        return PostSorter.sort(queryset)

    def get_context_data(self, **kwargs):
        context = super(TopicShow, self).get_context_data(**kwargs)
        context['main_post'] = self.main_post
        return context


class PostVote(View):
    """
    JSON response of number of votes after voting (either up or down)
    """
    model = Post

    def vote(self, post, up=True):
        post = get_object_or_404(self.model, id=post)
        votes = post.vote.upvote() if up else post.vote.downvote()
        return votes

    def upvote(self, request, post):
        upvotes = self.vote(post, True)
        return JsonResponse({
            'post': post,
            'votes': upvotes,
            'votes_type': 'up'
        })

    def downvote(self, request, post):
        downvotes = self.vote(post, False)
        return JsonResponse({
            'post': post,
            'votes': downvotes,
            'votes_type': 'down'
        })
