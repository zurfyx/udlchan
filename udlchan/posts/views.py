from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, View
from .models import Category, Topic, Comment
from .forms import CategoryForm, TopicForm, CommentForm
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
    template_name = 'posts/category_add.html'

    def get_success_url(self):
        return reverse('posts:category')


class TopicList(ListView):
    """
    Shows list of topics in a Category.
    """
    model = Topic
    template_name = 'posts/topics.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category,
                                          title=self.kwargs['category'])
        return self.model.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TopicShow(ListView):
    """
    Shows a specific topic, and its comments.
    """
    model = Topic
    template_name = 'posts/topic.html'

    def get_queryset(self):
        self.object = get_object_or_404(self.model, id=self.kwargs['pk'])
        self.comments = Comment.objects.filter(topic=self.object)

    def get_context_data(self, **kwargs):
        context = super(TopicShow, self).get_context_data(**kwargs)
        context['object'] = self.object
        context['comments'] = self.comments
        return context


class TopicAdd(CreateView):
    """
    Create a new topic.
    """
    pass


class CommentAdd(CreateView):
    """
    Add a comment to a topic.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'posts/comment_create.html'


class CommentVote(View):
    """
    JSON response of number of votes after voting (either up or down)
    """
    model = Comment

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
