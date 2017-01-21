from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Subject)
admin.site.register(models.ProfessorSubject)
admin.site.register(models.Professor)
admin.site.register(models.UserProfile)
admin.site.register(models.Post)
admin.site.register(models.Student)
admin.site.register(models.StudentGroup)
admin.site.register(models.Group)
admin.site.register(models.Comment)
admin.site.register(models.Vote)
admin.site.register(models.Attachment)
admin.site.register(models.Attempt)
admin.site.register(models.Quiz)
admin.site.register(models.QuizQuestion)
admin.site.register(models.Answer)
admin.site.register(models.Teach)
admin.site.register(models.Question)
