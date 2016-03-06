from __future__ import unicode_literals

from django.db import models


class AbstractTimeStamped(models.Model):
    """
    Auto-updated created and modified fields
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractCategory(AbstractTimeStamped):
    """
    A category will consist of a title and a description.
    """
    title = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        verbose_name_plural='categories'


class AbstractPost(AbstractTimeStamped):
    """
    A publication consist of a title and content.
    It will always belong to a category.
    It might have a parent post.
    """
    title = models.CharField(max_length=300, default='')
    content = models.CharField(max_length=10000, default='')
    category = models.ForeignKey('posts.Post', verbose_name='Post')
    user = models.CharField(max_length=30)  # TODO

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
