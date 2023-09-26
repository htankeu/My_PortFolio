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
    logo = models.ImageField(null=True, default="skills.png")
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



class Message(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    subject = models.CharField(max_length=200,null=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name



class Endorsement(models.Model):
    name = models.CharField(max_length=200, null=True)
    body = models.TextField()
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.body[0:50]

class comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]