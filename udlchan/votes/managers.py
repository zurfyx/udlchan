from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import F
from django.utils import timezone
from .models import Vote


class _VoteManager(models.Manager):
    def __init__(self, through, model, instance):
        self.through = through
        self.model = model
        self.instance = instance

    def _object(self):
        db_entry = self.through.objects.filter(content_object=self.instance)
        return db_entry[0] if db_entry else \
            self.through(content_object=self.instance)

    def up(self):
        return self._object().up

    def down(self):
        return self._object().down

    def upvote(self):
        obj = self._object()
        obj.up += 1
        obj.save()
        return obj.up

    def downvote(self):
        obj = self._object()
        obj.down += 1
        obj.save()
        return obj.down

    def reset(self):
        obj = self._object()
        obj.up = obj.down = 0
        obj.save()


class VoteManager(GenericRelation):
    def __init__(self, through=Vote, manager=_VoteManager, **kwargs):
        self.through = through
        self.manager = manager
        super(VoteManager, self).__init__(self.through, **kwargs)

    def __get__(self, instance, model):
        manager = self.manager(
            through=self.through,
            model=model,
            instance=instance,
        )
        return manager

    def contribute_to_class(self, cls, name):
        super(VoteManager, self).contribute_to_class(cls, name)
        setattr(cls, name, self)
