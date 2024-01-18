from django.db import models
from user.models import User
# Create your models here.

class Thought(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=16)
    image = models.ImageField(upload_to="thought_image/", default='default.jpg')
    date_time = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.title}'
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE, related_name= 'comment')
    text = models.CharField(max_length = 264)
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'commented {self.text}'



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)

    def __str__(self):
        return f'liked {self.user}'


class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)

    def __str__(self):
        return f'shared by {self.user}'


class Comment_reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name= 'reply')
    text = models.CharField(max_length = 264, default="comment reply")


    def __str__(self):
        return f'replied {self.user}'