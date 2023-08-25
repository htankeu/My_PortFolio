from django.shortcuts import render
from .models import Project, Skill, SprachSkills

# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    sprachSkills = SprachSkills.objects.all()
    context = {'projects': projects, 'skills': skills, 'sprachSkills': sprachSkills}
    return render(request, 'base/index.html', context)

def projectPage(request, pk):
    project = Project.objects.get(id=pk)

    return render(request, 'base/project.html', {'project': project})