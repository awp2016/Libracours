from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


def get_avatar_upload_path(instance, filename):
    username = instance.user.username
    return 'media/{0}/avatar/{1}'.format(username, filename)


def get_attachment_upload_path(instance, filename):
    username = instance.user.username
    return 'media/{0}/attachments/%Y/%m/%d/{1}'.format(username, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = 'UserProfile', on_delete=models.CASCADE)
    birthdate = models.DateField()
    avatar = models.ImageField(upload_to=get_avatar_upload_path)


class Domain(models.Model):
    name = models.CharField(max_length=64)


class Student(models.Model):
    user_id = models.OneToOneField(UserProfile, primary_key=True,
                                   on_delete=models.CASCADE)
    score = models.IntegerField()


class Group(models.Model):
    leader = models.OneToOneField(Student, null=True,
                                  on_delete=models.SET_NULL)
    year = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)


class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.CharField(max_length=256)


class Profesor(models.Model):
    user_id = models.OneToOneField(UserProfile, primary_key=True,
                                   on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)


class ProfesorStudent(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    author = models.ForeignKey(UserProfile, null=True,
                               on_delete=models.SET_NULL)
    prof_subject = models.ForeignKey(ProfesorStudent, null=True,
                                     on_delete=models.SET_NULL)
    date = models.DateField()
    title = models.CharField(max_length=64)
    description = HTMLField()


class Attachment(models.Model):
    path = models.FileField(upload_to=get_attachment_upload_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)


class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    vote_type = models.BooleanField()  # True - upvote, False - downvote


class Answer(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()


class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Teach(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
