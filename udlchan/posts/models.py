from __future__ import unicode_literals

from django.db import models
from .abstract_models import AbstractCategory, AbstractPost


class Category(AbstractCategory):
    pass


class Post(AbstractPost):
    pass
