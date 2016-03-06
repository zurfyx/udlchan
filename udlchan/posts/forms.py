from django import forms
from .models import Category, Post


class CategoryForm(forms.ModelForm):
    description = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ['title', 'description']


class PostForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']
