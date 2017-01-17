from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def get_avatar_upload_path(instance, filename):
    username = instance.user.username
    return 'media/{0}/avatar/{1}'.format(username, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    avatar = models.ImageField(upload_to=get_avatar_upload_path)
