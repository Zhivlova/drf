from django.db import models
from uuid import uuid4


class User(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)


class Header(models.Model):
    logo_icon = models.ImageField
    logo_text = models.CharField(max_length=64)


class Footer(models.Model):
    fag = models.FilePathField
    contacts = models.IntegerField
    copyright = models.CharField(max_length=64)
