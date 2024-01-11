from django.db import models
from user.models import User
# Create your models here.

class Thought(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField()
    image = models.ImageField(upload_to="thought_image/")
    date_time = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'
    

class Comment(models.Model):
    user = models.ForeignKey(User)
    thought = models.ForeignKey(Thought)
    text = models.CharField(max_length = 264)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'commented {self.text}'


class Like(models.Model):
    user = models.ForeignKey(User)
    thought = models.ForeignKey(Thought)

    def __str__(self):
        return f'liked {self.user}'


class Share(models.Model):
    user = models.ForeignKey(User)
    thought = models.ForeignKey(Thought)

    def __str__(self):
        return f'shared by {self.user}'


class Comment_reply(models.Model):
    user = models.ForeignKey(User)
    thought = models.ForeignKey(Thought)
    comment = models.ForeignKey(Comment)

    def __str__(self):
        return f'replied {self.user}'