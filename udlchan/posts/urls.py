from django.conf.urls import url

from .views import CategoryList, CategoryAdd, CategoryPostList
from .views import TopicShow
from .views import PostVote

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

    # List of posts in a category
    url(
        r'^category/(?P<category>\w+)$',
        CategoryPostList.as_view(),
        name='category_posts'
    ),

    # Show topic = main post + descendant posts
    url(
        r'^topic/(?P<post>\d+)$',
        TopicShow.as_view(),
        name='category_topic'
    ),

    # Upvote post
    url(
        r'topic/(?P<post>\d+)/up',
        PostVote().upvote,
        name='post_upvote'
    ),

    # Downvote post
    url(
        r'topic/(?P<post>\d+)/down',
        PostVote().downvote,
        name='post_downvote'
    ),
]