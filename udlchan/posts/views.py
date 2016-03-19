from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, CreateView, RedirectView
from .models import Category, Topic, Comment
from .forms import CategoryForm, TopicForm, CommentForm
from .utils import PostSorter
from .mixins import CommentAddAJAXMixin


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
    template_name = 'posts/category_create.html'

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
        self.object = get_object_or_404(self.model, id=self.kwargs['topic'])
        self.comments = Comment.objects.filter(topic=self.object)

    def get_context_data(self, **kwargs):
        context = super(TopicShow, self).get_context_data(**kwargs)
        context['object'] = self.object
        context['comments'] = self.comments
        form_initial = {'topic':self.kwargs['topic']}
        context['form'] = CommentForm(initial=form_initial)
        return context


class TopicAdd(CreateView):
    """
    Create a new topic.
    """
    model = Topic
    form_class = TopicForm
    template_name = 'posts/topic_create.html'

    def get_initial(self):
        category = get_object_or_404(Category, title=self.kwargs['category'])
        return {
            'category': category
        }

    def get_success_url(self):
        return reverse('posts:category',
                       kwargs={'category': self.kwargs['category']})

    def get_context_data(self, **kwargs):
        context = super(TopicAdd, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context


class CommentAdd(CommentAddAJAXMixin, RedirectView):
    """
    Add a comment to a topic. Redirects to topic if not an AJAX request.
    """
    permanent = False
    query_string = True
    pattern_name = 'posts:topic'

    def get_redirect_url(self, *args, **kwargs):
        return super(CommentAdd, self).get_redirect_url(*args, **kwargs)


class VoteGeneric(View):
    """
    JSON response of number of votes after voting (either up or down)
    """
    model = None

    def __init__(self, model):
        self.model = model

    def vote(self, object, up=True):
        object = get_object_or_404(self.model, id=object)
        votes = object.vote.upvote() if up else object.vote.downvote()
        return votes

    def upvote(self, request, object):
        upvotes = self.vote(object, True)
        return JsonResponse({
            'object_id': object,
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


class TopicVote(VoteGeneric):
    model = Topic

    def __init__(self):
        super(TopicVote, self).__init__(self.model)

    def upvote(self, request, topic):
        return super(TopicVote, self).upvote(request, topic)

    def downvote(self, request, topic):
        return super(TopicVote, self).downvote(request, topic)


class CommentVote(VoteGeneric):
    model = Comment

    def __init__(self):
        super(CommentVote, self).__init__(self.model)

    def upvote(self, request, comment):
        return super(CommentVote, self).upvote(request, comment)

    def downvote(self, request, comment):
        return super(CommentVote, self).downvote(request, comment)
