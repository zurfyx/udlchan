from django.conf.urls import url

from .views import CategoriesList, CategoriesAdd

urlpatterns = [
    # Add new category
    url(
        r'^add$',
        CategoriesAdd.as_view(),
        name='categories_add'
    ),

    # List of categories
    url(
        r'^$',
        CategoriesList.as_view(),
        name='categories'
    ),
]