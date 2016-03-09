from django.conf.urls import url

from .views import CategoryList, CategoryAdd
from .views import CategoryPostList

urlpatterns = [
    # List of categories
    url(
        r'^$',
        CategoryList.as_view(),
        name='categories'
    ),

    # Add new category
    url(
        r'^category/add$',
        CategoryAdd.as_view(),
        name='categories_add'
    ),

    # List of posts in a category
    url(
        r'^category/(?P<category>\w+)$',
        CategoryPostList.as_view(),
        name='category_posts'
    )
]