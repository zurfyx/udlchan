from __future__ import unicode_literals

from django.db import models


class AbstractVote(models.Model):
    """
    Keeps track of upvotes and downvotes.
    """
    up = models.IntegerField()
    down = models.IntegerField()

    class Meta:
        abstract = True
