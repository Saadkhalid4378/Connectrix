from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=12, blank=True, null=True )
    city = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'upload/', blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user}'
    