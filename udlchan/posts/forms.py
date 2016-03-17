from django import forms
from .models import Category, Topic, Comment


class CategoryForm(forms.ModelForm):
    description = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ['title', 'description']


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['category', 'title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', 'parent']
