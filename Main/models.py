from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import date


def get_avatar_upload_path(instance, filename):
    username = instance.user.username
    return 'media/{0}/avatar/{1}'.format(username, filename)


def get_attachment_upload_path(instance, filename):
    current_date = date.today()
    username = instance.post.author.user.username

    return 'media/{0}/attachments/{1}/{2}/{3}/{4}'.format(username,
                                                          current_date.year,
                                                          current_date.month,
                                                          current_date.day,
                                                          filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User,
                                related_name='userProfile',
                                on_delete=models.CASCADE)
    birthdate = models.DateField()
    avatar = models.ImageField(upload_to=get_avatar_upload_path)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Domain(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(UserProfile, related_name='Student',
                                on_delete=models.CASCADE, default=None)
    score = models.IntegerField()

    def __str__(self):
        return self.user.user.username

    def __unicode__(self):
        return self.user.user


class Question(models.Model):
    text = models.CharField(max_length=256)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class Subject(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Professor(models.Model):
    user_id = models.OneToOneField(UserProfile, related_name='Professor',
                                   on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, through='ProfessorSubject')


    def __str__(self):
        return self.user_id.user.username

    def __unicode__(self):
        return self.user_id.user.username


class ProfessorSubject(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
                                  related_name='professor_subject')
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL,
                                default = None, related_name='subject')

    def __str__(self):
        return self.professor.user_id.user.username + ' ' + self.subject.name

    def __unicode__(self):
        return self.professor.user_id.user.username + ' ' + self.subject.name


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    leader = models.OneToOneField(Student, null=True,
                                  on_delete=models.SET_NULL, related_name='leader')
    year = models.IntegerField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    professor_subjects = models.ManyToManyField(ProfessorSubject)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.id


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    author = models.ForeignKey(UserProfile, null=True,
                               on_delete=models.SET_NULL)
    prof_subject = models.ForeignKey(ProfessorSubject, null=True,
                                     on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Attachment(models.Model):
    path = models.FileField(upload_to=get_attachment_upload_path)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.path.name


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    vote_type = models.BooleanField()  # True - upvote, False - downvote

    def __str__(self):
        return self.comment

    def __unicode__(self):
        return self.comment


class Answer(models.Model):
    text = models.CharField(max_length=256)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class Quiz(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.author

    def __unicode__(self):
        return self.author


class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.IntegerField()
