from django import forms
from .models import Category, Topic, Comment


class CategoryForm(forms.ModelForm):
    description = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ['title', 'slug', 'description']
        labels = {
            'slug': 'URL (i.e. online-games)'
        }


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['category', 'title', 'content']
        widgets = {
            'category': forms.HiddenInput
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['topic', 'parent', 'content']
        widgets = {
            'topic': forms.HiddenInput,
            'parent': forms.HiddenInput,
            'content': forms.Textarea(attrs={'placeholder': 'Content'})
        }
