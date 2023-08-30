from django.shortcuts import render,redirect
from .models import Project, Skill, SprachSkills
from .form import ProjectForm

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

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/project_form.html', {'form': form})


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/project_form.html', {'form': form})