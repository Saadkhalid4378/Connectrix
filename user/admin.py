from django.contrib import admin
from user.models import User, Profile
# Register your models here.

class User_profile(admin.ModelAdmin):
    list_display = ['id', 'username']

admin.site.register(User, User_profile)
admin.site.register(Profile)