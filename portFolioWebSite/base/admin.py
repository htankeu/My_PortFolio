from django.contrib import admin

# Register your models here.

from .models import Project,Skill,Tag, SprachSkills

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(SprachSkills)