from django.contrib import admin
from thought.models import Thought, Comment, Like, Share, Comment_reply
# Register your models here.

@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'thought', 'user', 'date_time']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'thought']


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'thought']


@admin.register(Comment_reply)
class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'thought', 'comment']

