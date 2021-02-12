from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=40)
    address = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=200)
    country = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='user_img')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))

    image_tag.short_description = 'Image'