from django.contrib import admin
from .models import Category, Topic, Comment


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'topic', 'created')

admin.site.register(Category)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)
