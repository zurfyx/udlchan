from django.conf.urls import url

from .views import CategoriesList

urlpatterns = [
    # List of categories
    url(
        r'^$',
        CategoriesList.as_view(),
        name='categories'
    ),
]