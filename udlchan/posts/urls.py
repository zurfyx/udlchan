from django.conf.urls import url

from .views import CategoryList, CategoryAdd
from .views import TopicList, TopicShow
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
        name='category_posts'
    ),

    # Show topic
    url(
        r'^topic/(?P<pk>\d+)$',
        TopicShow.as_view(),
        name='category_topic'
    ),

    # Add new comment
    url(
        r'^topic/(?P<topic>\d+)/comment$',
        CommentAdd.as_view(),
        name='comment_add'
    ),

    # Upvote post
    url(
        r'^topic/(?P<post>\d+)/up$',
        CommentVote().upvote,
        name='post_upvote'
    ),

    # Downvote post
    url(
        r'^topic/(?P<post>\d+)/down$',
        CommentVote().downvote,
        name='post_downvote'
    ),
]