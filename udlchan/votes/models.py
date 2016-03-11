from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .abstract_models import AbstractVote


class VoteManger(models.Manager):
    def filter(self, *args, **kwargs):
        if 'content_object' in kwargs:
            content_object = kwargs.pop('content_object')
            content_type = ContentType.objects.get_for_model(content_object)
            kwargs.update({
                    'content_type':content_type,
                    'object_id':content_object.pk
                    })
        return super(VoteManger, self).filter(*args, **kwargs)


class Vote(AbstractVote):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = VoteManger()

    class Meta:
        unique_together = ('content_type', 'object_id')
