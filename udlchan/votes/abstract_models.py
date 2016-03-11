from __future__ import unicode_literals

from django.db import models


class AbstractVote(models.Model):
    """
    Keeps track of upvotes.
    """
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

    def __str__(self):
        return str(self.up) + '/' + str(self.down)

    class Meta:
        abstract = True
