from django.db import models
import uuid
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, null=True)
    thumbnail = models.ImageField(null=True)
    thumbnail2 = models.ImageField(null=True)
    body = RichTextUploadingField(null=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class SprachSkills(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=36,null=True)
    bg_color = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    



class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title