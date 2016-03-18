from __future__ import unicode_literals

from django.db import models
from .abstract_models import AbstractTimeStamped
from votes.managers import VoteManager


class Category(AbstractTimeStamped):
    """
    A category will consist of a title and a description.
    """
    title = models.CharField(db_index=True, unique=True, max_length=300,
                             default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Topic(AbstractTimeStamped):
    """
    A topic represents forum "thread" first post.
    It will always belong to a category and it will contain comments.
    """
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=10000, default='')
    vote = VoteManager()

    def __str__(self):
        return self.title


class Comment(AbstractTimeStamped):
    """
    A comment will consist of text content (description).
    It will belong to a topic, and it can be nested into other parent Comment.
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True,
                               verbose_name='Parent',
                               on_delete=models.CASCADE,
                               related_name='post_parent')
    content = models.CharField(max_length=10000, default='')
    vote = VoteManager()

    def __str__(self):
        return self.content if self.content <= 30 else self.content[:30] + '...'
