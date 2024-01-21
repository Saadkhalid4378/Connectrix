from django.contrib import admin
from user.models import User, Profile
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'date_of_birth', 'city', 'image']