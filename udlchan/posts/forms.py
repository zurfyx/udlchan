from django.forms import ModelForm
from .models import Category, Post


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class PostForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
