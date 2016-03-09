from __future__ import unicode_literals

from django.db import models
from .abstract_models import AbstractTimeStamped


class Category(AbstractTimeStamped):
    """
    A category will consist of a title and a description.
    """
    title = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Post(AbstractTimeStamped):
    """
    A publication consist of a title and content.
    It will always belong to a category.
    It might have a parent post.
    """
    title = models.CharField(max_length=300, default='')
    content = models.CharField(max_length=10000, default='')
    category = models.ForeignKey(Category, default='', verbose_name='Category')
    parent = models.ForeignKey('self', null=True, verbose_name='Parent')
    user = models.CharField(max_length=30)  # TODO

    def __str__(self):
        return self.title
