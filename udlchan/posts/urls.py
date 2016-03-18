from django.conf.urls import url

from .views import CategoryList, CategoryAdd
from .views import TopicList, TopicShow, TopicAdd, TopicVote
from .views import CommentAdd, CommentVote

urlpatterns = [
    # List of categories
    url(
        r'^$',
        CategoryList.as_view(),
        name='category'
    ),

    # Add new category
    url(
        r'^category/add$',
        CategoryAdd.as_view(),
        name='category_add'
    ),

    # List of topics in a category
    url(
        r'^category/(?P<category>\w+)$',
        TopicList.as_view(),
        name='category'
    ),

    # Add new topic
    url(
        r'^category/(?P<category>\w+)/topic$',
        TopicAdd.as_view(),
        name='topic_add'
    ),

    # Show topic
    url(
        r'^topic/(?P<topic>\d+)$',
        TopicShow.as_view(),
        name='topic'
    ),

    # Add new comment
    url(
        r'^topic/(?P<topic>\d+)/comment$',
        CommentAdd.as_view(),
        name='comment_add'
    ),

    # Upvote topic
    url(
        r'^topic/(?P<topic>\d+)/up$',
        TopicVote().upvote,
        name='topic_upvote'
    ),

    # Downvote topic
    url(
        r'^topic/(?P<topic>\d+)/down$',
        TopicVote().downvote,
        name='topic_downvote'
    ),

    # Upvote comment
    url(
        r'^commnent/(?P<comment>\d+)/up$',
        CommentVote().upvote,
        name='comment_upvote'
    ),

    # Downvote comment
    url(
        r'^comment/(?P<comment>\d+)/down$',
        CommentVote().downvote,
        name='comment_downvote'
    ),
]