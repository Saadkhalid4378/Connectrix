from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneRel(User)
    phone = models.CharField(max_length = 12)
    city = models.CharField()
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to = 'upload/')

    def __str__(self):
        return f'Profile of {self.user}'