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

class Domain(models.Model):
    name = models.CharField(max_length=64)

class StudentGroup(models.Model):
    pass #TO DO

class Group(models.Model):
    leader = models.OneToOneField(StudentGroup, null=True, on_delete=models.SET_NULL)
    year = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
	
class Question(models.Model):
	text = models.CharField(max_length=256)

