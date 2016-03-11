from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from .abstract_models import AbstractTimeStamped
from votes.managers import VoteManager


class Category(AbstractTimeStamped):
    """
    A category will consist of a title and a description.
    """
    title = models.CharField(unique=True, max_length=300, default='')
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

    Main refers to the first post. It will be null for the main post, and it
    will contain the reference on the child posts.
    Parent refers to the parent post. It will be null for any post but the
    nested ones.

    It will make use votes app to register posts upvotes / downvotes, as a
    1 to 1 field.
    """
    title = models.CharField(max_length=300, default='')
    content = models.CharField(max_length=10000, default='')
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE)
    main = models.ForeignKey('self', null=True, verbose_name='Main',
                             related_name='post_main')
    parent = models.ForeignKey('self', null=True, verbose_name='Parent',
                               related_name='post_parent')
    user = models.CharField(max_length=30)  # TODO
    vote = VoteManager()

    def __str__(self):
        return self.title
