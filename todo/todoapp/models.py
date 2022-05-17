from django.db import models
from uuid import uuid4
from mainapp.models import User


class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=64)
    link = models.FilePathField
    project_users = models.ManyToManyField(User)


class TODO(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    todo_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    todo_user = models.OneToOneField(User, on_delete=models.CASCADE)
