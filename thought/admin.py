from django.contrib import admin
from thought.models import Thought, Comment
# Register your models here.

class Thought_detail(admin.ModelAdmin):
    list_display = ['pk', 'user', 'title']

admin.site.register(Thought, Thought_detail)
admin.site.register(Comment)
