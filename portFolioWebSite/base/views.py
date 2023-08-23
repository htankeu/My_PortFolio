from django.shortcuts import render
from .models import Project, Skill, SprachSkills

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    sprachSkills = SprachSkills.objects.all()
    return render(request,'base/index.html',{'projects':projects,
                                             'skills':skills,
                                             'sprachSkills':sprachSkills})